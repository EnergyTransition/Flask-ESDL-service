#  This work is based on original code developed and copyrighted by TNO 2020.
#  Subsequent contributions are licensed to you by the developers of such code and are
#  made available to the Project under one or several contributor license agreements.
#
#  This work is licensed to you under the Apache License, Version 2.0.
#  You may obtain a copy of the license at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Contributors:
#      TNO         - Initial implementation
#  Manager:
#      TNO

import logging
import base64
import urllib
from application.esdl_service import es_process
from flask import request
from flask_restplus import Resource, fields
from application.api import api
import json

log = logging.getLogger(__name__)

ns = api.namespace('esdl_service', description='Operations to process an energy system described in ESDL')


post_body = api.model('PostBody', {
    "energysystem": fields.String
})


@ns.route('/count_esdl_objects', methods=['POST'])
class CountESDLObjectsPost(Resource):

    @api.expect(post_body)
    def post(self):
        post_body = json.loads(request.get_data().decode("utf-8"))

        es_b64_bytes = post_body["energysystem"].encode('utf-8')
        es_bytes = base64.decodebytes(es_b64_bytes)
        esdl_string = es_bytes.decode('utf-8')

        esdl_processor = es_process.EnergySystemProcessor()
        return esdl_processor.count_esdl_class_instances(esdl_string)
