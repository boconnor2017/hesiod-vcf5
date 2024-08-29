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

# Test parameters - DO NOT INCLUDE THIS IN COPY
lab_environment_json = env_json_py
vcsa8_json_str = libjson.populate_var_from_json_file("lib/vcs-deploy-config", "vcsa8_json_template.json")
vcsa8_json_py = libjson.load_json_variable(vcsa8_json_str)
vcsa_template_json = vcsa8_json_py

# Start by initializing from the template
vcsa_new_json = vcsa_template_json
# Make changes to json_py variable 

print(vcsa_new_json["new_vcsa"]["esxi"]["hostname"] +"="+ lab_environment_json["physical_server"][0]["ip_address"])
print(vcsa_new_json["new_vcsa"]["esxi"]["username"] +"="+ lab_environment_json["physical_server"][0]["username"])
print(vcsa_new_json["new_vcsa"]["esxi"]["password"] +"="+ lab_environment_json["physical_server"][0]["password"])
print(vcsa_new_json["new_vcsa"]["esxi"]["deployment_network"] +"="+ lab_environment_json["vcenter_server"]["deployment_network"])
print(vcsa_new_json["new_vcsa"]["esxi"]["datastore"] +"="+ lab_environment_json["vcenter_server"]["deployment_datastore"])
print(vcsa_new_json["new_vcsa"]["appliance"]["name"] +"="+ lab_environment_json["vcenter_server"]["vm_name"])
print(vcsa_new_json["new_vcsa"]["network"]["system_name"] +"="+ lab_environment_json["vcenter_server"]["fqdn"])
print(vcsa_new_json["new_vcsa"]["network"]["ip"] +"="+ lab_environment_json["vcenter_server"]["ip"])
print(vcsa_new_json["new_vcsa"]["network"]["prefix"] +"="+ lab_environment_json["vcenter_server"]["cidr_size"])
print(vcsa_new_json["new_vcsa"]["network"]["gateway"] +"="+ lab_environment_json["vcenter_server"]["default_gateway"])
print(vcsa_new_json["new_vcsa"]["network"]["dns_servers"][0] +"="+ lab_environment_json["dns"][0])
print(vcsa_new_json["new_vcsa"]["os"]["password"] +"="+ lab_environment_json["universal_authentication"]["universal_password"])
print(vcsa_new_json["new_vcsa"]["os"]["ntp_servers"] +"="+ lab_environment_json["ntp"]["server"])
print(vcsa_new_json["new_vcsa"]["sso"]["password"] +"="+ lab_environment_json["universal_authentication"]["universal_password"])

