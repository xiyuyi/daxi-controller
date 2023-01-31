from daxi.control.process.facilitator.processes_facilitator import save_process_configs
from daxi.control.process.facilitator.system.demos.demo_acquisition_parameter_suggestion_mode7 import \
    demo_acquisition_params_mode7
from daxi.globals_configs_constants_general_tools_needbettername.constants import process_templates, \
    params_test_selected_params, configs_daq_terminals
from daxi.control.process.facilitator.system.tools.acquisition_parameter_suggestion import AcqParamMode1
from daxi.globals_configs_constants_general_tools_needbettername.parser import NIDAQConfigsParser
import os

import pprint

# Prints the nicely formatted dictionary
m = demo_acquisition_params_mode7()

acquisition_parameters = m.selected_parameters

path = os.path.join(process_templates, 'template_acquisition_mode7-dev.yaml')

# create a configuration dictionary.
configs_dict = {}

# 1. get the acquisition parameter dictionary


process_parameters = m.selected_parameters

# load in all the devices' configuration dictionary
p = NIDAQConfigsParser()
# now get the terminal configurations
p.set_configs_path(configs_daq_terminals)
section = 'Connection Section'
keyword = 'nidaq_terminals'
daq_terminal_configs = \
    p.get_configs_by_path_section_keyword(section, keyword, verbose=False)

keyword = 'calibration_records'
calibration_records = \
    p.get_configs_by_path_section_keyword(section, keyword, verbose=False)

keyword = 'alignment_records'
alignment_records = \
    p.get_configs_by_path_section_keyword(section, keyword, verbose=False)

keyword = 'camera_core_configs'
camera_core_configs = \
    p.get_configs_by_path_section_keyword(section, keyword, verbose=False)

keyword = 'stage_core_configs'
stage_core_configs = \
    p.get_configs_by_path_section_keyword(section, keyword, verbose=False)

# composite the configs_dict dictionary
configs_dict={
        "process type": "acquisition, mode 7",
        "process configs":
        {
            "process type": "acquisition, mode 7",
            "acquisition parameters": acquisition_parameters,
        },
        "device configurations":
        {
            'nidaq_terminals': daq_terminal_configs,
            'calibration_records': calibration_records,
            'alignment_records': alignment_records,
            'camera_core_configs': camera_core_configs,
            'stage_core_configs': stage_core_configs,
        },
}
# save the configurations dictionary as a yaml file.
save_process_configs(path=path, configs=configs_dict)
pprint.pprint(configs_dict)