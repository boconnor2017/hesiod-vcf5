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
vcf_json_str = libjson.populate_var_from_json_file("json", "vcf5_bringup_template.json")
vcf_json_py = libjson.load_json_variable(vcf_json_str)
this_script_name = os.path.basename(__file__)
logfile_name = env_json_py["logs"][this_script_name]

# # # # # # # # # # # # # # # # # # # #
# SANDBOX AREA BELOW
# # # # # # # # # # # # # # # # # # # #

#test_subnet = "192.168.10.1"
new_vcf_json_py = vcf_json_py
# Complexity that isn't needed in the prompt... keeping it simple... your welcome world.
vsan_subnet = new_vcf_json_py["networkSpecs"][1]["subnet"].split(".")
new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["startIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"7"
new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["endIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"48"
new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][1]["startIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"3"
new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][1]["endIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"6"
new_vcf_json_py["networkSpecs"][1]["includeIpAddress"][0] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"50"
new_vcf_json_py["networkSpecs"][1]["includeIpAddress"][1] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"49"
# Back to standard programming...
print(new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["startIpAddress"])
print(new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["endIpAddress"])
print(new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][1]["startIpAddress"])
print(new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][1]["endIpAddress"])
print(new_vcf_json_py["networkSpecs"][1]["includeIpAddress"][0])
print(new_vcf_json_py["networkSpecs"][1]["includeIpAddress"][1])