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
import json
import urllib

from flask import request
from flask_restx import Namespace, Resource
from flask_accepts import accepts

from application.api.schema import CountRequestSchema, CountRequest
from application.esdl_service import es_process
from application.api import api

log = logging.getLogger(__name__)

api = Namespace('esdl_service', path="/", description='Operations to process an energy system described in ESDL')


@api.route('/count_esdl_objects')
class CountESDLObjects(Resource):

    @accepts(schema=CountRequestSchema, api=api)
    def post(self):
        query_params: CountRequest = request.parsed_obj

        # post_body = json.loads(request.get_data().decode("utf-8"))

        es_b64_bytes = query_params.energysystem.encode('utf-8')
        es_bytes = base64.decodebytes(es_b64_bytes)
        esdl_string = es_bytes.decode('utf-8')

        esdl_processor = es_process.EnergySystemProcessor()
        return esdl_processor.count_esdl_class_instances(esdl_string)
