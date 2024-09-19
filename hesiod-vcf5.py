# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import deploy_dns as dnslib
from lib import deploy_vcenter as vcslib
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

# Hesiod Header and Log init
liblog.hesiod_print_header()
liblog.hesiod_log_header(logfile_name)
err = "Successfully imported Hesiod python libraries."
liblog.write_to_logs(err, logfile_name)
err = "Succesfully initialized logs to "+logfile_name
liblog.write_to_logs(err, logfile_name)
err = ""
liblog.write_to_logs(err, logfile_name)

# Local functions
def _main_():
    print("Deploying ESXi environment ready for VCF Bringup.")
    print("IMPORTANT: while this is running, deploy Cloud Builder manually.")
    print("The reason cloud builder is manual is because there are extra resources (mainly storage) needed to automate the automation. Even though it is POSSIBLE to automate it, the goal of this project is to use minimal resources.")
    print("")
    print("Estimated runtime: 20min.")
    print("")
    prereq_validation_check_1 = False 
    prereq_validation_check_1 = esxlib.prereq_validate_ova()
    if prereq_validation_check_1 is False:
        sys.exit()
    else:
        physical_server_number = int(input("Select the physical host number you want to deploy to (use 0 if you only have one physical server): "))
        host_number = 0
        err = "    Initiating class for host: "+str(host_number)
        liblog.write_to_logs(err, logfile_name)
        nested_esxi_class = esxlib.populate_nested_esxi_class_from_json(env_json_py, host_number, physical_server_number)
        err = "    Deploying: "+nested_esxi_class.name_of_vm+" Size: "+nested_esxi_class.numCPU+"CPU, "+nested_esxi_class.memoryGB+"GB Memory, and "+nested_esxi_class.harddiskCapacityGB+"GB storage."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.deploy_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        seconds = 90
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete initial boot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Sizing VM."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.size_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete sizing reboot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        host_number = 1
        err = "    Initiating class for host: "+str(host_number)
        liblog.write_to_logs(err, logfile_name)
        nested_esxi_class = esxlib.populate_nested_esxi_class_from_json(env_json_py, host_number, physical_server_number)
        err = "    Deploying: "+nested_esxi_class.name_of_vm+" Size: "+nested_esxi_class.numCPU+"CPU, "+nested_esxi_class.memoryGB+"GB Memory, and "+nested_esxi_class.harddiskCapacityGB+"GB storage."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.deploy_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        seconds = 90
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete initial boot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Sizing VM."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.size_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete sizing reboot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        host_number = 2
        err = "    Initiating class for host: "+str(host_number)
        liblog.write_to_logs(err, logfile_name)
        nested_esxi_class = esxlib.populate_nested_esxi_class_from_json(env_json_py, host_number, physical_server_number)
        err = "    Deploying: "+nested_esxi_class.name_of_vm+" Size: "+nested_esxi_class.numCPU+"CPU, "+nested_esxi_class.memoryGB+"GB Memory, and "+nested_esxi_class.harddiskCapacityGB+"GB storage."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.deploy_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        seconds = 90
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete initial boot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Sizing VM."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.size_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete sizing reboot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        host_number = 3
        err = "    Initiating class for host: "+str(host_number)
        liblog.write_to_logs(err, logfile_name)
        nested_esxi_class = esxlib.populate_nested_esxi_class_from_json(env_json_py, host_number, physical_server_number)
        err = "    Deploying: "+nested_esxi_class.name_of_vm+" Size: "+nested_esxi_class.numCPU+"CPU, "+nested_esxi_class.memoryGB+"GB Memory, and "+nested_esxi_class.harddiskCapacityGB+"GB storage."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.deploy_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        seconds = 90
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete initial boot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Sizing VM."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.size_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete sizing reboot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Preparing ESXi host for VCF."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.prep_esxi_hosts_for_vcf(env_json_py, physical_server_number)
        print("")
        print("")
        print("")
        print("Your Nested ESXi Hosts are prepped. You may now login to CloudBuilder and begin bringup.")
        print("Use cp /usr/local/drop/lab.json json/lab_environment.json to pull your saved lab config details.")
        print("Use cp /usr/local/drop/vcf.json json/vcf5_bringup_template.json to pull your saved vcf config details.")
    
def deploy_dns():
    print("Deploying Tanium DNS Server.")
    err = "    configure_tanium_prerequisites(): "
    liblog.write_to_logs(err, logfile_name)
    cmd_returned_value = dnslib.configure_tanium_prerequisites()
    err = "    cmd_returned_value: "+str(cmd_returned_value)
    liblog.write_to_logs(err, logfile_name)
    libgen.pause_python_for_duration(5)
    err = "    configure_os_name_resolution(ip): "
    liblog.write_to_logs(err, logfile_name)
    dnslib.configure_os_name_resolution("8.8.8.8")
    libgen.pause_python_for_duration(5)
    err = "    install_tanium(): "
    liblog.write_to_logs(err, logfile_name)
    cmd_returned_value = dnslib.install_tanium()
    err = "    cmd_returned_value: "+str(cmd_returned_value)
    liblog.write_to_logs(err, logfile_name)
    libgen.pause_python_for_duration(60)
    err = "    get_ip_address(): "
    liblog.write_to_logs(err, logfile_name)
    ip = dnslib.get_ip_address("eth0")
    err = "    ip address of DNS Server: "+ip
    liblog.write_to_logs(err, logfile_name)
    err = "    get_tanium_token(): "
    liblog.write_to_logs(err, logfile_name)
    token = dnslib.get_tanium_token("admin", "admin", ip)
    err = "    token: "+token
    liblog.write_to_logs(err, logfile_name)
    err = "    change_tanium_password(): "
    liblog.write_to_logs(err, logfile_name)
    dnslib.change_tanium_password(token, ip, env_json_py["universal_authentication"]["universal_password"])
    sys.exit()

def deploy_vcsa():
    prereq_validation_check_1 = False 
    prereq_validation_check_2 = False
    prereq_validation_check_1 = vcslib.prereq_validate_iso()
    prereq_validation_check_2 = vcslib.prereq_validate_dns_record()
    if prereq_validation_check_1 is False:
        sys.exit()
    elif prereq_validation_check_2 is False:
        sys.exit()
    else:
        print("Deploying vCenter Server.")
        err = "    mount_vcsa_iso_to_os(): "
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = vcslib.mount_vcsa_iso_to_os()
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        err = "    Importing vcsa8_json_template.json"
        liblog.write_to_logs(err, logfile_name)
        vcsa8_json_str = libjson.populate_var_from_json_file("lib/vcs-deploy-config", "vcsa8_json_template.json")
        err = "    Converting json to python variable."
        liblog.write_to_logs(err, logfile_name)
        vcsa8_json_py = libjson.load_json_variable(vcsa8_json_str)
        err = "    generate_json_file():"
        liblog.write_to_logs(err, logfile_name)
        new_vcsa_json_py = vcslib.generate_json_file(vcsa8_json_py, env_json_py)
        err = "    dump_json_to_file():"
        liblog.write_to_logs(err, logfile_name)      
        json_filename = "vcsa.json"  # keep it simple
        libjson.dump_json_to_file(new_vcsa_json_py, json_filename)
        err = "    install_vcenter_server():"
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = vcslib.install_vcenter_server(json_filename)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)

def deploy_esx():
    prereq_validation_check_1 = False 
    prereq_validation_check_1 = esxlib.prereq_validate_ova()
    if prereq_validation_check_1 is False:
        sys.exit()
    else:
        print("Deploying Nested ESXi Server.")
        host_number = int(input("Select the host number you want to deploy from \"host specs\" (0-3): "))
        physical_server_number = int(input("Select the physical host number you want to deploy to (use 0 if you only have one physical server): "))
        err = "    User selected host: "+str(host_number)
        liblog.write_to_logs(err, logfile_name)
        nested_esxi_class = esxlib.populate_nested_esxi_class_from_json(env_json_py, host_number, physical_server_number)
        err = "    Deploying: "+nested_esxi_class.name_of_vm+" Size: "+nested_esxi_class.numCPU+"CPU, "+nested_esxi_class.memoryGB+"GB Memory, and "+nested_esxi_class.harddiskCapacityGB+"GB storage."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.deploy_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        seconds = 90
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete initial boot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Sizing VM."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.size_nested_esxi(nested_esxi_class)
        err = "    cmd_returned_value: "+str(cmd_returned_value)
        liblog.write_to_logs(err, logfile_name)
        err = "    Pausing for "+str(seconds)+" to allow ESXi server to complete sizing reboot."
        liblog.write_to_logs(err, logfile_name)
        esxlib.pause_python_for_duration(seconds)
        err = "    Preparing ESXi host for VCF."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.prep_esxi_hosts_for_vcf(env_json_py, physical_server_number)
        err = "    Rebooting ESXi hosts."
        liblog.write_to_logs(err, logfile_name)
        cmd_returned_value = esxlib.reboot_esxi_hosts(env_json_py)
        err = "Finished!"
        liblog.write_to_logs(err, logfile_name)


def help_stdout():
    print("HELP MENU: hesiod-vcf5.py [options]")
    print("Enter options 1x per run, do not add all parameters at once!")
    print("--help option to see this menu.")
    print("-lev     option to prompt for lab environment variables.")
    print("-vcf     option to prompt for vcf bringup variables.")
    print("-dns     option to deploy a DNS server.")
    print("-vcs     option to deploy a vCenter server.")
    print("-esx     option to deploy a nested ESXi server.")
    print("None     default, assumes all config files are populated and DNS is available.")
    print("")
    print("")

def match_dns(args):
    if '-dns' in args:
        return True

def match_help(args):
    if '--help' in args:
        return True

def match_esx(args):
    if '-esx' in args:
        return True

def match_lev(args):
    if '-lev' in args:
        return True

def match_vcf(args):
    if '-vcf' in args:
        return True

def match_vcs(args):
    if '-vcs' in args:
        return True

def prompt_lab_environment_config():
    print("Runnung Hesiod Lab JSON prompt function.")
    new_env_json_py = env_json_py
    print("")
    print("Part 1 of 7 - Physical Network.")
    print("** This is the network that your physical hosts are connected to. **")
    new_env_json_py["physical_network"][0]["default_gateway"] = input("Default Gateway: ")
    new_env_json_py["physical_network"][0]["subnet_mask"] = input("Subnet Mask (example: 255.255.255.0): ")
    new_env_json_py["physical_network"][0]["cidr"] = input("CIDR (example: 24): ")
    print("")
    print("Part 2 of 7 - VCF VLANs.")
    print("** These are the physical VLANs that will be used for VCF. **")
    new_env_json_py["physical_network"][1]["default_gateway"] = input("Management Default Gateway: ")
    new_env_json_py["physical_network"][1]["subnet_mask"] = input("Management Subnet Mask (example: 255.255.255.0): ")
    new_env_json_py["physical_network"][1]["cidr"] = input("Management CIDR (example: 24): ")
    print("")
    new_env_json_py["physical_network"][2]["default_gateway"] = input("VSAN Default Gateway: ")
    new_env_json_py["physical_network"][2]["subnet_mask"] = input("VSAN Subnet Mask (example: 255.255.255.0): ")
    new_env_json_py["physical_network"][2]["cidr"] = input("VSAN CIDR (example: 24): ")
    print("")
    new_env_json_py["physical_network"][3]["default_gateway"] = input("TEP Default Gateway: ")
    new_env_json_py["physical_network"][3]["subnet_mask"] = input("TEP Subnet Mask (example: 255.255.255.0): ")
    new_env_json_py["physical_network"][3]["cidr"] = input("TEP CIDR (example: 24): ")
    print("")
    new_env_json_py["physical_network"][4]["default_gateway"] = input("vMotion Default Gateway: ")
    new_env_json_py["physical_network"][4]["subnet_mask"] = input("vMotion Subnet Mask (example: 255.255.255.0): ")
    new_env_json_py["physical_network"][4]["cidr"] = input("vMotion CIDR (example: 24): ")
    print("")
    print("Part 3 of 7 - Physical Servers.")
    print("** You only need one. BUT you can have as many as you want. **")
    physical_server_count = int(input("How many physical servers do you have for this environment? "))
    i = 0
    while i < physical_server_count:
        print("*** Server Number "+str(i+1)+" ***")
        new_env_json_py["physical_server"][i]["username"] = "root" #hardcoded
        new_env_json_py["physical_server"][i]["password"] = input("Password: ")
        new_env_json_py["physical_server"][i]["ip_address"] = input("IP Address: ")
        i = i+1
    print("")
    print("Part 4 of 7 - Universal Authentication.")
    print("** This is so you don't have to keep typing passwords. **")
    new_env_json_py["universal_authentication"]["universal_password"] = input("Universal Password to configure on all VMware appliances (example: VMware123!): ")
    new_env_json_py["universal_authentication"]["universal_long_password"] = input("Universal LONG Password to configure on all VMware appliances (recommended: VMware123!VMware123!): ")
    new_env_json_py["universal_authentication"]["vcenter_administrator_sso_login"] = input("Default vCenter Administrator SSO login (recommended: administrator@vsphere.local): ")
    print("")
    print("Part 5 of 7 - Domain.")
    print("** For all things DNS and NTP. **")
    dns_server_count = int(input("How many DNS servers do you have for this environment? "))
    i = 0
    while i < dns_server_count:
        print("*** DNS Server "+str(i+1)+" ***")
        new_env_json_py["dns"][i] = input("IP Address: ")
        i = i+1
    new_env_json_py["ntp"]["server"] = input("NTP Server: ")
    new_env_json_py["domain"] = input("Domain: ")
    print("")
    print("Part 6 of 7 - vCenter.")
    print("** For development teams who need a vCenter. If you don't need a vCenter you can keep these parameters blank. **")
    new_env_json_py["vcenter_server"]["deployment_network"] = input("Name of the deployment network on your physical host (example: VM Network): ")
    new_env_json_py["vcenter_server"]["deployment_datastore"] = input("Name of the deployment datastore on your physical host (example: datastore1): ")
    new_env_json_py["vcenter_server"]["vm_name"] = input("Name of the VCSA virtual machine: ")
    new_env_json_py["vcenter_server"]["fqdn"] = input("FQDN of the vCenter Server: ")
    new_env_json_py["vcenter_server"]["ip"] = input("IP Address of the vCenter Server: ")
    new_env_json_py["vcenter_server"]["cidr_size"] = input("CIDR of the vCenter Server (example: 24): ")
    new_env_json_py["vcenter_server"]["default_gateway"] = input("Default Gateway of the vCenter Server: ")
    print("")
    print("Part 7 of 7 - Nested ESXi.")
    print("** The specs for the nested ESXi hosts (you need these for your VCF environment). **")
    new_env_json_py["nested_esxi_servers"]["universal_specs"]["deployment_network"] = input("(ALL ESXI HOSTS) Name of the deployment network on your physical host (example: VM Network): ")
    new_env_json_py["nested_esxi_servers"]["universal_specs"]["deployment_datastore"] = input("(ALL ESXI HOSTS) Name of the deployment datastore on your physical host (example: datastore1): ")
    new_env_json_py["nested_esxi_servers"]["universal_specs"]["dir_path_to_ova_and_filename"] = input("The path to the nested esxi ova on the photon server (example: /usr/local/drop/Nested_ESXi8.0u3_Appliance_Template_v1.ova): ")
    new_env_json_py["nested_esxi_servers"]["universal_specs"]["numCPU"] = input("(ALL ESXI HOSTS) Number of CPUs (Recommended: 8): ")
    new_env_json_py["nested_esxi_servers"]["universal_specs"]["memoryGB"] = input("(ALL ESXI HOSTS) Memory in GB (Recommended: 32): ")
    new_env_json_py["nested_esxi_servers"]["universal_specs"]["harddiskcapacityGB"] = input("(ALL ESXI HOSTS) Hard Disk Capacity in GB (Recommended: 100): ")
    esxi_server_count = 4 #hardcoded
    i = 0
    while i < esxi_server_count:
        print("*** ESXi Server "+str(i+1)+" ***")
        new_env_json_py["nested_esxi_servers"]["host_specs"][i]["name_of_vm"] = input("VM Name: ")
        new_env_json_py["nested_esxi_servers"]["host_specs"][i]["esxi_hostname"] = input("ESXi Hostname: ")
        new_env_json_py["nested_esxi_servers"]["host_specs"][i]["esxi_ip_address"] = input("ESXi IP Address: ")
        i = i+1
    lab_json_filename = "lab.json"
    libjson.dump_json_to_file(new_env_json_py, lab_json_filename)
    print("")
    print("Completed!")
    print("Your configuration is stored in a file called "+lab_json_filename+".")
    print("To save this configuration for future use, run: mv lab.json /usr/local/drop/lab.json")
    sys.exit()

def prompt_vcf_bringup_template(vcf_json_py):
    print("Running VCF5 Prerequisites JSON prompt function.")
    new_vcf_json_py = vcf_json_py
    print("Part 1 of 11: SDDC Manager Spec:")
    new_vcf_json_py["sddcManagerSpec"]["hostname"] = input("SDDC Manager Hostname (default: "+vcf_json_py["sddcManagerSpec"]["hostname"]+"): ")
    new_vcf_json_py["sddcManagerSpec"]["ipAddress"] = input("SDDC IP Address (default: "+vcf_json_py["sddcManagerSpec"]["ipAddress"]+"): ")
    new_vcf_json_py["sddcManagerSpec"]["netmask"] = input("SDDC Netmask (default: "+vcf_json_py["sddcManagerSpec"]["netmask"]+"): ")
    new_vcf_json_py["sddcManagerSpec"]["localUserPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    new_vcf_json_py["sddcManagerSpec"]["rootUserCredentials"]["password"] = env_json_py["universal_authentication"]["universal_long_password"]
    new_vcf_json_py["sddcManagerSpec"]["secondUserCredentials"]["password"] = env_json_py["universal_authentication"]["universal_long_password"]
    print("")
    print("Part 2 of 11: Random stuff the BU decided to keep separate...:")
    new_vcf_json_py["sddcId"] = input("SDDC ID (default: "+vcf_json_py["sddcId"]+"): ")
    new_vcf_json_py["esxLicense"] = input("ESX License (default: "+vcf_json_py["esxLicense"]+"): ")
    new_vcf_json_py["ntpServers"][0] = env_json_py["ntp"]["server"]
    print("")
    print("Part 3 of 11: DNS Spec:")
    new_vcf_json_py["dnsSpec"]["subdomain"] = input("Subdomain (default: "+vcf_json_py["dnsSpec"]["subdomain"]+"): ")
    new_vcf_json_py["dnsSpec"]["domain"] = input("Domain (default: "+vcf_json_py["dnsSpec"]["domain"]+"): ")
    new_vcf_json_py["dnsSpec"]["nameserver"] = env_json_py["dns"][0]
    new_vcf_json_py["dnsSpec"]["secondaryNameserver"] = env_json_py["dns"][1]
    print("")
    print("Part 4 of 11: Network Specs:")
    new_vcf_json_py["networkSpecs"][0]["subnet"] = input("Management Subnet (default: "+vcf_json_py["networkSpecs"][0]["subnet"]+"): ")
    new_vcf_json_py["networkSpecs"][0]["gateway"] = input("Management Gateway (default: "+vcf_json_py["networkSpecs"][0]["gateway"]+"): ")
    new_vcf_json_py["networkSpecs"][1]["subnet"] = input("VSAN Subnet (default: "+vcf_json_py["networkSpecs"][1]["subnet"]+"): ")
    new_vcf_json_py["networkSpecs"][1]["gateway"] = input("VSAN Gateway (default: "+vcf_json_py["networkSpecs"][1]["gateway"]+"): ")
    # Complexity that isn't needed in the prompt... keeping it simple... your welcome world.
    vsan_subnet = new_vcf_json_py["networkSpecs"][1]["subnet"].split(".")
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["startIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"7"
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][0]["endIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"48"
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][1]["startIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"3"
    new_vcf_json_py["networkSpecs"][1]["includeIpAddressRanges"][1]["endIpAddress"] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"6"
    new_vcf_json_py["networkSpecs"][1]["includeIpAddress"][0] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"50"
    new_vcf_json_py["networkSpecs"][1]["includeIpAddress"][1] = vsan_subnet[0]+"."+vsan_subnet[1]+"."+vsan_subnet[2]+"."+"49"
    # Back to standard programming...
    new_vcf_json_py["networkSpecs"][2]["subnet"] = input("VMOTION Subnet (default: "+vcf_json_py["networkSpecs"][2]["subnet"]+"): ")
    new_vcf_json_py["networkSpecs"][2]["gateway"] = input("VMOTION Gateway (default: "+vcf_json_py["networkSpecs"][2]["gateway"]+"): ")
    # More complexitizing. 
    vmotion_subnet = new_vcf_json_py["networkSpecs"][2]["subnet"].split(".")
    new_vcf_json_py["networkSpecs"][2]["includeIpAddressRanges"][0]["startIpAddress"] = vmotion_subnet[0]+"."+vmotion_subnet[1]+"."+vmotion_subnet[2]+"."+"3"
    new_vcf_json_py["networkSpecs"][2]["includeIpAddressRanges"][0]["endIpAddress"] = vmotion_subnet[0]+"."+vmotion_subnet[1]+"."+vmotion_subnet[2]+"."+"50"
    # And... we're back.
    print("")
    print("Part 5 of 11: NSX-T Specs:")
    libjson.dump_json_to_file(new_vcf_json_py, "vcf.json") 
    new_vcf_json_py["nsxtSpec"]["nsxtManagerSize"] = input("NSX Manager Size (default: "+vcf_json_py["nsxtSpec"]["nsxtManagerSize"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][0]["hostname"] = input("NSX Manager A Hostname (default: "+vcf_json_py["nsxtSpec"]["nsxtManagers"][0]["hostname"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][0]["ip"] = input("NSX Manager A IP Address (default: "+vcf_json_py["nsxtSpec"]["nsxtManagers"][0]["ip"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][1]["hostname"] = input("NSX Manager B Hostname (default: "+vcf_json_py["nsxtSpec"]["nsxtManagers"][1]["hostname"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][1]["ip"] = input("NSX Manager B IP Address (default: "+vcf_json_py["nsxtSpec"]["nsxtManagers"][1]["ip"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][2]["hostname"] = input("NSX Manager C Hostname (default: "+vcf_json_py["nsxtSpec"]["nsxtManagers"][2]["hostname"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtManagers"][2]["ip"] = input("NSX Manager C IP Address (default: "+vcf_json_py["nsxtSpec"]["nsxtManagers"][2]["ip"]+"): ")
    new_vcf_json_py["nsxtSpec"]["rootNsxtManagerPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    new_vcf_json_py["nsxtSpec"]["nsxtAdminPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    new_vcf_json_py["nsxtSpec"]["nsxtAuditPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    new_vcf_json_py["nsxtSpec"]["overLayTransportZone"]["zoneName"] = input("Overlay Transport Zone Name (default: "+vcf_json_py["nsxtSpec"]["overLayTransportZone"]["zoneName"]+"): ")
    new_vcf_json_py["nsxtSpec"]["overLayTransportZone"]["networkName"] = input("Overlay Transport Zone Network Name (default: "+vcf_json_py["nsxtSpec"]["overLayTransportZone"]["networkName"]+"): ")
    new_vcf_json_py["nsxtSpec"]["vlanTransportZone"]["zoneName"] = input("VLAN Transport Zone Name (default: "+vcf_json_py["nsxtSpec"]["vlanTransportZone"]["zoneName"]+"): ")
    new_vcf_json_py["nsxtSpec"]["vlanTransportZone"]["networkName"] = input("VLAN Transport Zone Network Name (default: "+vcf_json_py["nsxtSpec"]["vlanTransportZone"]["networkName"]+"): ")
    new_vcf_json_py["nsxtSpec"]["vip"] = input("NSX Manager Cluster VIP (default: "+vcf_json_py["nsxtSpec"]["vip"]+"): ")
    new_vcf_json_py["nsxtSpec"]["vipFqdn"] = input("NSX Manager Cluster VIP FQDN (default: "+vcf_json_py["nsxtSpec"]["vipFqdn"]+"): ")
    new_vcf_json_py["nsxtSpec"]["nsxtLicense"] = input("NSX License (default: "+vcf_json_py["nsxtSpec"]["nsxtLicense"]+"): ")
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["name"] = input("ESXi Host Overlay TEP IP Pool (default: "+vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["name"]+"): ")
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"][0]["start"] = input("IP Pool Ranges START (default: "+vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"][0]["start"]+"): ")
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"][0]["end"] = input("IP Pool Ranges END (default: "+vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["ipAddressPoolRanges"][0]["end"]+"): ")
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["cidr"] = input("CIDR (default: "+vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["cidr"]+"): ")
    new_vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["gateway"] = input("Gateway (default: "+vcf_json_py["nsxtSpec"]["ipAddressPoolSpec"]["subnets"][0]["gateway"]+"): ")
    print("")
    print("Part 6 of 11: vSAN Specs:")
    new_vcf_json_py["vsanSpec"]["vsanName"] = input("VSAN Datastore Name (default: "+vcf_json_py["vsanSpec"]["vsanName"]+"): ")
    new_vcf_json_py["vsanSpec"]["licenseFile"] = input("VSAN License (default: "+vcf_json_py["vsanSpec"]["licenseFile"]+"): ")
    new_vcf_json_py["vsanSpec"]["datastoreName"] = new_vcf_json_py["vsanSpec"]["vsanName"]
    print("")
    print("Part 7 of 11: DVS Specs:")
    new_vcf_json_py["dvsSpecs"][0]["dvsName"] = input("DVS Name (default: "+vcf_json_py["dvsSpecs"][0]["dvsName"]+"): ")
    print("")
    print("Part 8 of 11: Cluster Specs:")
    new_vcf_json_py["clusterSpec"]["clusterName"] = input("Compute Cluster Name (default: "+vcf_json_py["clusterSpec"]["clusterName"]+"): ")
    print("")
    print("Part 9 of 11: PSC Specs:")
    new_vcf_json_py["pscSpecs"][0]["pscSsoSpec"]["ssoDomain"] = input("SSO Domain (default: "+vcf_json_py["pscSpecs"][0]["pscSsoSpec"]["ssoDomain"]+"): ")
    new_vcf_json_py["pscSpecs"][0]["adminUserSsoPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    print("")
    print("Part 10 of 11: vCenter Specs:")
    new_vcf_json_py["vcenterSpec"]["vcenterIp"] = input("Management Domain vCenter IP (default: "+vcf_json_py["vcenterSpec"]["vcenterIp"]+"): ")
    new_vcf_json_py["vcenterSpec"]["vcenterHostname"] = input("Management Domain vCenter Hostname (default: "+vcf_json_py["vcenterSpec"]["vcenterHostname"]+"): ")
    new_vcf_json_py["vcenterSpec"]["licenseFile"] = input("vCenter License (default: "+vcf_json_py["vcenterSpec"]["licenseFile"]+"): ")
    new_vcf_json_py["vcenterSpec"]["rootVcenterPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    print("")
    print("Part 11 of 11: Management Host Specs:")
    # Bulk prompt
    esxi_host_subnet = input("ESXi Host Subnet (default: 255.255.255.0): ")
    esxi_host_cidr = input("ESXi Host CIDR (default 10.0.0.0/24): ")
    esxi_host_gateway = input("ESXi Host Gateway (default: 10.0.0.250): ")
    esxi_association = input("ESXi Host Associated Datacenter (default: sfo-m01-dc01): ")
    new_vcf_json_py["hostSpecs"][0]["credentials"]["password"] = env_json_py["universal_authentication"]["universal_password"]
    new_vcf_json_py["hostSpecs"][0]["ipAddressPrivate"]["subnet"] = esxi_host_subnet
    new_vcf_json_py["hostSpecs"][0]["ipAddressPrivate"]["cidr"] = esxi_host_cidr
    new_vcf_json_py["hostSpecs"][0]["ipAddressPrivate"]["gateway"] = esxi_host_gateway
    new_vcf_json_py["hostSpecs"][0]["ipAddressPrivate"]["ipAddress"] = input("ESXi 1 IP Address (default: "+vcf_json_py["hostSpecs"][0]["ipAddressPrivate"]["ipAddress"]+"): ")
    new_vcf_json_py["hostSpecs"][0]["hostname"] = input("ESXi 1 Hostname (default: "+vcf_json_py["hostSpecs"][0]["hostname"]+"): ")
    new_vcf_json_py["hostSpecs"][0]["association"] = esxi_association
    new_vcf_json_py["hostSpecs"][1]["credentials"]["password"] = env_json_py["universal_authentication"]["universal_password"]
    new_vcf_json_py["hostSpecs"][1]["ipAddressPrivate"]["subnet"] = esxi_host_subnet
    new_vcf_json_py["hostSpecs"][1]["ipAddressPrivate"]["cidr"] = esxi_host_cidr
    new_vcf_json_py["hostSpecs"][1]["ipAddressPrivate"]["gateway"] = esxi_host_gateway
    new_vcf_json_py["hostSpecs"][1]["ipAddressPrivate"]["ipAddress"] = input("ESXi 2 IP Address (default: "+vcf_json_py["hostSpecs"][1]["ipAddressPrivate"]["ipAddress"]+"): ")
    new_vcf_json_py["hostSpecs"][1]["hostname"] = input("ESXi 2 Hostname (default: "+vcf_json_py["hostSpecs"][1]["hostname"]+"): ")
    new_vcf_json_py["hostSpecs"][1]["association"] = esxi_association
    new_vcf_json_py["hostSpecs"][2]["credentials"]["password"] = env_json_py["universal_authentication"]["universal_password"]
    new_vcf_json_py["hostSpecs"][2]["ipAddressPrivate"]["subnet"] = esxi_host_subnet
    new_vcf_json_py["hostSpecs"][2]["ipAddressPrivate"]["cidr"] = esxi_host_cidr
    new_vcf_json_py["hostSpecs"][2]["ipAddressPrivate"]["gateway"] = esxi_host_gateway
    new_vcf_json_py["hostSpecs"][2]["ipAddressPrivate"]["ipAddress"] = input("ESXi 3 IP Address (default: "+vcf_json_py["hostSpecs"][2]["ipAddressPrivate"]["ipAddress"]+"): ")
    new_vcf_json_py["hostSpecs"][2]["hostname"] = input("ESXi 3 Hostname (default: "+vcf_json_py["hostSpecs"][2]["hostname"]+"): ")
    new_vcf_json_py["hostSpecs"][2]["association"] = esxi_association
    new_vcf_json_py["hostSpecs"][3]["credentials"]["password"] = env_json_py["universal_authentication"]["universal_password"]
    new_vcf_json_py["hostSpecs"][3]["ipAddressPrivate"]["subnet"] = esxi_host_subnet
    new_vcf_json_py["hostSpecs"][3]["ipAddressPrivate"]["cidr"] = esxi_host_cidr
    new_vcf_json_py["hostSpecs"][3]["ipAddressPrivate"]["gateway"] = esxi_host_gateway
    new_vcf_json_py["hostSpecs"][3]["ipAddressPrivate"]["ipAddress"] = input("ESXi 4 IP Address (default: "+vcf_json_py["hostSpecs"][3]["ipAddressPrivate"]["ipAddress"]+"): ")
    new_vcf_json_py["hostSpecs"][3]["hostname"] = input("ESXi 4 Hostname (default: "+vcf_json_py["hostSpecs"][3]["hostname"]+"): ")
    new_vcf_json_py["hostSpecs"][3]["association"] = esxi_association
    vcf_json_filename = "vcf.json"
    libjson.dump_json_to_file(new_vcf_json_py, vcf_json_filename)
    print("")
    print("Completed!")
    print("Your configuration is stored in a file called "+vcf_json_filename+". ")
    print("To save this configuration for future use, run: mv vcf.json /usr/local/drop/vcf.json")
    sys.exit()


# Get args
err = "Getting args..."
liblog.write_to_logs(err, logfile_name)
arg_len = len(sys.argv) 
err = "    "+str(arg_len)+" args passed."
liblog.write_to_logs(err, logfile_name)

# Initialize default user options
user_options = ['n', 'n', 'n']

# Match args
match_found = False 
match_found = match_help(sys.argv)
if match_found :
    err = "    --help found. Initiating standard output."
    liblog.write_to_logs(err, logfile_name)
    help_stdout()
    err = "    Exiting script."
    liblog.write_to_logs(err, logfile_name)
    sys.exit() 

else:
  match_found = False 
  match_found = match_dns(sys.argv)
  if match_found :
      err = "    -dns found. Initiating DNS build."
      liblog.write_to_logs(err, logfile_name)
      deploy_dns()
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_lev(sys.argv)
  if match_found :
      err = "    -lev found. Initiating lab environment prompts."
      liblog.write_to_logs(err, logfile_name)
      prompt_lab_environment_config()
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_vcf(sys.argv)
  if match_found :
      err = "    -vcf found. Initiating vcf bringup prompts."
      liblog.write_to_logs(err, logfile_name)
      prompt_vcf_bringup_template(vcf_json_py)
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_vcs(sys.argv)
  if match_found :
      err = "    -vcs found. Initiating vCenter deployment."
      liblog.write_to_logs(err, logfile_name)
      deploy_vcsa()
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_esx(sys.argv)
  if match_found :
      err = "    -esx found. Initiating vCenter deployment."
      liblog.write_to_logs(err, logfile_name)
      deploy_esx()
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

err = "No arguments found. Instantiating _main_()"
liblog.write_to_logs(err, logfile_name)
_main_()