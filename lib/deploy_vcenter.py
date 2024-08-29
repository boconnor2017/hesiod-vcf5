# Description: Builds vCenter Server using Photon OS
# Author: Brendan O'Connor
# Date: August 2024
# Version: 4.0

# Base imports
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni
import os
import stat 
import shutil
import urllib
import requests

'''
This script needs to run on a dedicated Photon OS server.
00. Prerequisites: run the quick start https://github.com/boconnor2017/hesiod-vcf5 
00. Prerequisites: manually attach the VCSA.iso to the Photon vm.
00. Prerequisites: create dns record for VCSA. 

Workflow:
01. Mount VCSA to Photon OS
    mkdir /usr/local/mount
    mount -t iso9660 -o loop /dev/cdrom /usr/local/mount/

02. Generate JSON file for VCSA deployment
    02a. Get config params from lab_environment.json
    02b. Write json file to OS

03. Install vCenter
'''
# General
def run_cmd_on_os(cmd):
    cmd_returned_value = os.system(cmd)
    return cmd_returned_value

# Prerequisite checks
def prereq_validate_iso():
    prereq_validation_check = input("Is the VCSA iso attached to this vm? (y/n): ")
    if 'y' in prereq_validation_check:
        return True 
    else:
        return False 
    
def prereq_validate_dns_record():
    prereq_validation_check = input("Is the dns record created for vCenter? (y/n): ")
    if 'y' in prereq_validation_check:
        return True 
    else:
        return False 
    
# Mount VCSA to Photon
def mount_vcsa_iso_to_os():
    cmd_returned_value = run_cmd_on_os("mkdir /usr/local/mount")
    cmd_returned_value = run_cmd_on_os("mount -t iso9660 -o loop /dev/cdrom /usr/local/mount/")
    return cmd_returned_value

# Generate JSON
def generate_json_file(vcsa_template_json, lab_environment_json):
    # Start by initializing from the template
    vcsa_new_json = vcsa_template_json
    vcsa_new_json["new_vcsa"]["esxi"]["hostname"] = lab_environment_json["physical_server"]["ip_address"]
    vcsa_new_json["new_vcsa"]["esxi"]["username"] = lab_environment_json["physical_server"]["username"]
    vcsa_new_json["new_vcsa"]["esxi"]["password"] = lab_environment_json["physical_server"]["password"]
    vcsa_new_json["new_vcsa"]["esxi"]["deployment_network"] = lab_environment_json["vcenter_server"]["deployment_network"]
    vcsa_new_json["new_vcsa"]["esxi"]["datastore"] = lab_environment_json["vcenter_server"]["deployment_datastore"]
    vcsa_new_json["new_vcsa"]["appliance"]["name"] = lab_environment_json["vcenter_server"]["vm_name"]
    vcsa_new_json["new_vcsa"]["network"]["system_name"] = lab_environment_json["vcenter_server"]["fqdn"]
    vcsa_new_json["new_vcsa"]["network"]["ip"] = lab_environment_json["vcenter_server"]["ip"]
    vcsa_new_json["new_vcsa"]["network"]["prefix"] = lab_environment_json["vcenter_server"]["cidr_size"]
    vcsa_new_json["new_vcsa"]["network"]["gateway"] = lab_environment_json["vcenter_server"]["default_gateway"]
    vcsa_new_json["new_vcsa"]["network"]["dns_servers"] = lab_environment_json["dns"]
    vcsa_new_json["new_vcsa"]["os"]["password"] = lab_environment_json["universal_authentication"]["universal_password"]
    vcsa_new_json["new_vcsa"]["os"]["ntp_servers"] = lab_environment_json["ntp"]["server"]
    vcsa_new_json["new_vcsa"]["sso"]["password"] = lab_environment_json["universal_authentication"]["universal_password"]
    return vcsa_new_json