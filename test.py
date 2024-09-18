# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import deploy_dns as dnslib
from lib import deploy_nested_esxi_hosts as esxlib

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

"""
ovftool --acceptAllEulas --skipManifestCheck --X:injectOvfEnv --net:"VM Network"="VM Network" --datastore="datastore1" --name="hesvcf-esx02" --powerOn --prop:guestinfo.hostname="hesvcf-esx02.hesiod.local" --prop:guestinfo.ipaddress="172.16.10.23" --prop:guestinfo.vlan="0" --prop:guestinfo.netmask="255.255.255.0" --prop:guestinfo.gateway="172.16.10.1" --prop:guestinfo.dns="172.16.10.9" --prop:guestinfo.domain="hesiod.local" --prop:guestinfo.ntp="pool.ntp.org" --prop:guestinfo.ssh=true --prop:guestinfo.syslog="192.168.0.1" --prop:guestinfo.password="VMware123!" --prop:guestinfo.createvmfs=false /usr/local/drop/Nested_ESXi8.0u3_Appliance_Template_v1.ova vi://"root":"VMware1!"@"172.16.0.203"

ovftool --acceptAllEulas --skipManifestCheck --X:injectOvfEnv --net:"VM Network"="VM Network" \
--datastore="datastore1" --name="DISKTEST-05" \
--prop:guestinfo.hostname="somethinginteresting" \
--prop:guestinfo.ipaddress="172.16.10.23" \
--prop:guestinfo.vlan="0" \
--prop:guestinfo.netmask="255.255.255.0" \
--prop:guestinfo.gateway="172.16.10.1" \
--prop:guestinfo.dns="172.16.10.9" \
--prop:guestinfo.domain="hesiod.local" \
--prop:guestinfo.ntp="pool.ntp.org" \
--prop:guestinfo.ssh=true \
--prop:guestinfo.syslog="192.168.0.1" \
--prop:guestinfo.password="VMware123!" \
--prop:guestinfo.createvmfs=false \
--powerOn \
--X:waitForIp \
/usr/local/drop/Nested_ESXi8.0u3_Appliance_Template_v1.ova \
vi://"root":"VMware1!"@"172.16.0.203"

$esxi1 = "172.16.10.23"
Connect-VIServer -Server $esxi1 -User root -Password VMware123!
$localDisk = Get-ScsiLun | where {$_.ExtensionData.DisplayName -match “Local LSI Disk”}
$canName = $localDisk.CanonicalName
$esxcli = Get-EsxCli -V2
$satp = ($esxcli.storage.nmp.device.list() | where {$_.Device -eq $canName }).StorageArrayType
$esxcli.storage.nmp.satp.rule.add($null,$null,$null,$canname,$null,$null,$null,”enable_ssd”,$null,$null,$satp,$null,$null,$null)
$esxcli.storage.core.claiming.reclaim($canName)
[/cc]
"""

nested_esxi_class = esxlib.populate_nested_esxi_class_from_json(env_json_py, 0, 0)
cmd = esxlib.get_ovftool_deploy_nested_esxi_cmd(nested_esxi_class)
print(cmd)