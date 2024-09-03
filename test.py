# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import deploy_dns as dnslib

# Import Standard Python libraries
import os
import sys

# Import json configuration parameters
env_json_str = libjson.populate_var_from_json_file("json", "lab_environment.json")
env_json_py = libjson.load_json_variable(env_json_str)
this_script_name = os.path.basename(__file__)
logfile_name = env_json_py["logs"][this_script_name]

# # # # # # # # # # # # # # # # # # # #
# SANDBOX AREA BELOW
# # # # # # # # # # # # # # # # # # # #

import test2 as config
import json

# Test parameters - DO NOT INCLUDE THIS IN COPY
lab_environment_json = env_json_py
vcsa8_json_str = libjson.populate_var_from_json_file("lib/vcs-deploy-config", "vcsa8_json_template.json")
vcsa8_json_py = libjson.load_json_variable(vcsa8_json_str)
vcsa_template_json = vcsa8_json_py

vcsa_config_json_as_string = {
    "__version": "2.13.0",
    "__comments": "https://github.com/boconnor2017/e2e-patterns",
    "new_vcsa": {
        "esxi": {
            "hostname": config.E2EP_ENVIRONMENT().esxi_host_ip,
            "username": config.E2EP_ENVIRONMENT().esxi_host_username,
            "password": config.E2EP_ENVIRONMENT().esxi_host_password,
            "deployment_network": config.E2EP_ENVIRONMENT().esxi_host_virtual_switch,
            "datastore": config.E2EP_ENVIRONMENT().esxi_host_datastore
        },
        "appliance": {
            "__comments": [
                "E2E Pattern: deploy vcsa"
            ],
            "thin_disk_mode": True,
            "deployment_option": "small",
            "name": config.VCSA().vcsa_vm_name
        },
        "network": {
            "ip_family": "ipv4",
            "mode": "static",
            "system_name": config.VCSA().fqdn,
            "ip": config.VCSA().ip,
            "prefix": config.E2EP_ENVIRONMENT().subnet_size,
            "gateway": config.E2EP_ENVIRONMENT().default_gw,
            "dns_servers": [
                config.DNS().ip
            ]
        },
        "os": {
            "password": config.UNIVERSAL().password,
            "ntp_servers": config.E2EP_ENVIRONMENT().ntp_server,
            "ssh_enable": False
        },
        "sso": {
            "password": config.UNIVERSAL().password,
            "domain_name": config.VCSA().sso_domain
        }
    },
    "ceip": {
        "description": {
            "__comments": [
                "E2E Pattern"
            ]
        },
        "settings": {
            "ceip_enabled": True
        }
    }
}
vcsa_config_json = json.dumps(vcsa_config_json_as_string)

libjson.dump_json_to_file(vcsa_config_json, "vcsa.json")