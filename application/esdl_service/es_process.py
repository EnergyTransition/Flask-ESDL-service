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

from esdl.esdl_handler import EnergySystemHandler
from esdl import esdl


class EnergySystemProcessor:

    def __init__(self):
        self.esh = EnergySystemHandler()

    def count_esdl_class_instances(self, esdl_string):
        self.esh.load_from_string(esdl_string)
        es = self.esh.get_energy_system()

        esdl_class_count_dict = dict()
        for es_element in es.eAllContents():
            if es_element.eClass.name in esdl_class_count_dict:
                esdl_class_count_dict[es_element.eClass.name] += 1
            else:
                esdl_class_count_dict[es_element.eClass.name] = 1

        return dict(sorted(esdl_class_count_dict.items()))


