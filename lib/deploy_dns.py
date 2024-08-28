# Description: Builds Tanium DNS Server on a Node Controller
# Author: Brendan O'Connor
# Date: August 2024
# Version: 4.0

# Base imports
import os
import shutil

'''
This script needs to run on the Photon OS vm that is going to be the dedicated DNS server.
00. Prerequisites: run the quick start https://github.com/boconnor2017/hesiod-vcf5 

Workflow:
01. Configure Tanium Prerequisites  
    02a. Run configure-tanium-ip-tables.sh script
        iptables -A INPUT -i eth0 -p udp --dport 53 -j ACCEPT
        sh /usr/local/e2e-patterns/dns/saveiptables.sh
            iptables-save >/etc/systemd/scripts/ip4save
        iptables -L
        systemctl disable systemd-resolved.service
        systemctl stop systemd-resolved
    02b. Run run-docker-compose.sh script 
02. Install Tanium
03. Change Default Password
    04a. Get Token using admin/admin 
    04b. Change password 
    04c. Get Token using permanent password 
'''
# General
def run_cmd_on_os(cmd):
    cmd_returned_value = os.system(cmd)
    return cmd_returned_value

# Configure Tanium Prerequisites
def configure_tanium_prerequisites():
    config_tanium_cmds = []
    config_tanium_cmds.append("iptables -A INPUT -i eth0 -p udp --dport 53 -j ACCEPT")
    config_tanium_cmds.append("iptables-save >/etc/systemd/scripts/ip4save")
    config_tanium_cmds.append("iptables -L")
    config_tanium_cmds.append("systemctl disable systemd-resolved.service")
    config_tanium_cmds.append("systemctl stop systemd-resolved")
    for x in config_tanium_cmds:
        cmd_returned_value = run_cmd_on_os(x)
        return cmd_returned_value

# Install Tanium
def install_tanium():
    print("install tanium")

# Change Tanium default password
def get_tanium_token():
    print("get tanium token")

def change_tanium_password(token):
    print("Change password")

