import os
import time 

"""
Sample Nested ESXi Class

class nested_esxi_class:
    deploy_to_this_port_group = "VM Network"
    deploy_to_this_datastore = "datastore1"
    name_of_vm = "TEST 006I"
    esxi_hostname = "test006"
    esxi_ip_address = "172.16.10.210"
    vlan = "0"
    netmask = "255.255.255.0"
    gateway = "172.16.10.1"
    dns = "172.16.10.9"
    domain = "hesiod.local"
    ntp = "pool.ntp.org"
    syslog_ip_address = "192.168.0.1"
    nested_esxi_password = "VMware123!"
    dir_path_of_ova = "/usr/local/drop/Nested_ESXi8.0u3_Appliance_Template_v1.ova"
    password_of_physical_host = "VMware1!"
    deploy_to_this_host = "172.16.0.203"
    numCPU = "8"
    memoryGB = "64"
    harddiskCapacityGB = "200"

"""

# General
def delete_script_file(script_file_name):
    if os.path.exists(script_file_name):
        os.remove(script_file_name)

def pause_python_for_duration(seconds):
    time.sleep(seconds)

def run_cmd_on_os(cmd):
    cmd_returned_value = os.system(cmd)
    return cmd_returned_value

def write_cmd_to_script_file(script, script_file_name):
    delete_script_file(script_file_name)
    script_file_name = open(script_file_name, "a")
    for line in script:
        script_file_name.writelines(line+'\n')
    script_file_name.close()

# OVFTool
def get_ovftool_deploy_nested_esxi_cmd(nested_esxi_class):
    cmd = "ovftool --acceptAllEulas --skipManifestCheck --X:injectOvfEnv "
    cmd = cmd+"--net:\""+nested_esxi_class.deploy_to_this_port_group+"\"=\""+nested_esxi_class.deploy_to_this_port_group+"\" "
    cmd = cmd+"--datastore=\""+nested_esxi_class.deploy_to_this_datastore+"\" "
    cmd = cmd+"--name=\""+nested_esxi_class.name_of_vm+"\" "
    cmd = cmd+"--powerOn "
    cmd = cmd+"--prop:guestinfo.hostname=\""+nested_esxi_class.esxi_hostname+"\" "
    cmd = cmd+"--prop:guestinfo.ipaddress=\""+nested_esxi_class.esxi_ip_address+"\" "
    cmd = cmd+"--prop:guestinfo.vlan=\""+nested_esxi_class.vlan+"\" "
    cmd = cmd+"--prop:guestinfo.netmask=\""+nested_esxi_class.netmask+"\" "
    cmd = cmd+"--prop:guestinfo.gateway=\""+nested_esxi_class.gateway+"\" "
    cmd = cmd+"--prop:guestinfo.dns=\""+nested_esxi_class.dns+"\" "
    cmd = cmd+"--prop:guestinfo.domain=\""+nested_esxi_class.domain+"\" "
    cmd = cmd+"--prop:guestinfo.ntp=\""+nested_esxi_class.ntp+"\" "
    cmd = cmd+"--prop:guestinfo.ssh=true "
    cmd = cmd+"--prop:guestinfo.syslog=\""+nested_esxi_class.syslog_ip_address+"\" "
    cmd = cmd+"--prop:guestinfo.password=\""+nested_esxi_class.nested_esxi_password+"\" "
    cmd = cmd+"--prop:guestinfo.createvmfs=false "
    cmd = cmd+nested_esxi_class.dir_path_of_ova+" "
    cmd = cmd+"vi://\"root\":\""+nested_esxi_class.password_of_physical_host+"\"@\""+nested_esxi_class.deploy_to_this_host+"\""
    return cmd

# PowerCLI
def get_pcli_set_powercliconfig_cmd():
    cmd = "Set-PowerCLIConfiguration -InvalidCertificateAction ignore"
    return cmd 

def get_pcli_connect_vi_server_cmd(nested_esxi_class):
    cmd = "Connect-VIserver -Server "+nested_esxi_class.deploy_to_this_host+" -User root -Password "+nested_esxi_class.password_of_physical_host
    return cmd 

def get_pcli_set_vm_cmd(nested_esxi_class):
    cmd = "Set-VM -VM \""+nested_esxi_class.name_of_vm+"\" -NumCPU "+nested_esxi_class.numCPU+" -MemoryGB "+nested_esxi_class.memoryGB
    return cmd 

def get_pcli_get_hard_disks_cmd(nested_esxi_class):
    cmd = "$nesxi_hard_disks = Get-HardDisk -VM \""+nested_esxi_class.name_of_vm+"\""
    return cmd 

def get_pcli_set_hard_disks_cmd(nested_esxi_class):
    cmd = "Set-HardDisk -HardDisk $nesxi_hard_disks[2] -CapacityGB "+nested_esxi_class.harddiskCapacityGB
    return cmd 

def get_pcli_power_off_cmd(nested_esxi_class):
    cmd = "Stop-VM -VM \""+nested_esxi_class.name_of_vm+"\""
    return cmd

def get_pcli_power_on_cmd(nested_esxi_class):
    cmd = "Start-VM -VM \""+nested_esxi_class.name_of_vm+"\""
    return cmd

# Custom
def deploy_nested_esxi(nested_esxi_class):
    deploy_nesxi_cmd = get_ovftool_deploy_nested_esxi_cmd(nested_esxi_class)
    cmd_returned_value = run_cmd_on_os(deploy_nesxi_cmd)
    return cmd_returned_value

def populate_nested_esxi_class_from_json(lab_json_py, host_number, physical_server_number):
    #lab_json_py is the python variable holding lab environment details
    #nested_esxi_class contains params for ONE esxi host at a time... therefore...
    #host_number is the list index for the given host (0-3 in a 4 node cluster)
    #hosts will be deployed to VCF Management Network by default
    class nested_esxi_class:
        deploy_to_this_port_group = lab_json_py["nested_esxi_servers"]["universal_specs"]["deployment_network"]
        deploy_to_this_datastore = lab_json_py["nested_esxi_servers"]["universal_specs"]["deployment_datastore"]
        name_of_vm = lab_json_py["nested_esxi_servers"]["host_specs"][host_number]["name_of_vm"]
        esxi_hostname = lab_json_py["nested_esxi_servers"]["host_specs"][host_number]["esxi_hostname"]
        esxi_ip_address = lab_json_py["nested_esxi_servers"]["host_specs"][host_number]["esxi_ip_address"]
        vlan = "0" #hardcoded
        netmask = lab_json_py["physical_network"][1]["subnet_mask"] #VCF Management Subnet
        gateway = lab_json_py["physical_network"][1]["default_gateway"] #VCF Management Subnet
        dns = lab_json_py["dns"][0] #Primary DNS server
        domain = lab_json_py["domain"]
        ntp = lab_json_py["ntp"]["server"]
        syslog_ip_address = "192.168.0.1" #hardcoded
        nested_esxi_password = lab_json_py["universal_authentication"]["universal_password"]
        dir_path_of_ova = lab_json_py["nested_esxi_servers"]["universal_specs"]["dir_path_to_ova_and_filename"]
        password_of_physical_host = lab_json_py["physical_server"][physical_server_number]["password"] 
        deploy_to_this_host = lab_json_py["physical_server"][physical_server_number]["ip_address"]
        numCPU = lab_json_py["nested_esxi_servers"]["universal_specs"]["numCPU"]
        memoryGB = lab_json_py["nested_esxi_servers"]["universal_specs"]["memoryGB"]
        harddiskCapacityGB = lab_json_py["nested_esxi_servers"]["universal_specs"]["harddiskcapacityGB"]
    return nested_esxi_class

def prereq_validate_ova():
    prereq_validation_check = input("Is the Nested ESXi 8.0u3 ova downloaded to /usr/local/drop? (y/n): ")
    if 'y' in prereq_validation_check:
        return True 
    else:
        return False 
    
def size_nested_esxi(nested_esxi_class):
    size_nesxi_cmd = []
    confirmation_cmd = " -Confirm:$false"
    cmd = get_pcli_set_powercliconfig_cmd()
    size_nesxi_cmd.append(cmd+confirmation_cmd)
    cmd = get_pcli_connect_vi_server_cmd(nested_esxi_class)
    size_nesxi_cmd.append(cmd)
    cmd = get_pcli_power_off_cmd(nested_esxi_class)
    size_nesxi_cmd.append(cmd+confirmation_cmd)
    cmd = get_pcli_set_vm_cmd(nested_esxi_class)
    size_nesxi_cmd.append(cmd+confirmation_cmd)
    cmd = get_pcli_get_hard_disks_cmd(nested_esxi_class)
    size_nesxi_cmd.append(cmd)
    cmd = get_pcli_set_hard_disks_cmd(nested_esxi_class)
    size_nesxi_cmd.append(cmd+confirmation_cmd)
    cmd = get_pcli_power_on_cmd(nested_esxi_class)
    size_nesxi_cmd.append(cmd+confirmation_cmd)
    write_cmd_to_script_file(size_nesxi_cmd, "size_nesxi.ps1")
    cmd = "pwsh size_nesxi.ps1"
    cmd_returned_value = run_cmd_on_os(cmd)
    return cmd_returned_value

