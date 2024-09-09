# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import deploy_dns as dnslib
from lib import deploy_vcenter as vcslib

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
    print("Standard run")

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

def help_stdout():
    print("HELP MENU: hesiod-vcf5.py [options]")
    print("Enter options 1x per run, do not add all parameters at once!")
    print("--help option to see this menu.")
    print("-lev     option to prompt for lab environment variables.")
    print("-vcf     option to prompt for vcf bringup variables.")
    print("-dns     option to deploy a DNS server.")
    print("-vcs     option to deploy a vCenter server.")
    print("None     default, assumes all config files are populated and DNS is available.")
    print("")
    print("")

def match_dns(args):
    if '-dns' in args:
        return True

def match_help(args):
    if '--help' in args:
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
    print("prompt lab env...")

"""
def prompt_user_for_options(user_options):
    prompt = input("Do you want to populate lab environment variables? [y/n] ")
    user_options.append(prompt)
    prompt = input("Do you want to populate vcf bringup variables? [y/n] ")
    user_options.append(prompt)
    prompt = input("Do you want to deploy a DNS server? [y/n] ")
    user_options.append(prompt)
    return user_options
"""

def prompt_vcf_bringup_template(vcf_json_py):
    print("Running VCF5 Prerequisites JSON prompt function.")
    new_vcf_json_py = vcf_json_py
    print("Part 1 of 11: SDDC Manager Spec:")
    new_vcf_json_py["sddcManagerSpec"]["hostname"] = input("SDDC Manager Hostname (default: "+vcf_json_py["sddcManagerSpec"]["hostname"]+"): ")
    new_vcf_json_py["sddcManagerSpec"]["ipAddress"] = input("SDDC IP Address (default: "+vcf_json_py["sddcManagerSpec"]["ipAddress"]+"): ")
    new_vcf_json_py["sddcManagerSpec"]["netmask"] = input("SDDC Netmask (default: "+vcf_json_py["sddcManagerSpec"]["netmask"]+"): ")
    new_vcf_json_py["sddcManagerSpec"]["localUserPassword"] = env_json_py["universal_authentication"]["universal_long_password"]
    new_vcf_json_py["sddcManagerSpec"]["rootUserCredentials"]["password"] = env_json_py["universal_authentication"]["universal_long_password"]
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
    new_vcf_json_py["nsxtSpec"]["nsxtAuditPasswor"] = env_json_py["universal_authentication"]["universal_long_password"]
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
    new_vcf_json_py["pscSpecs"][0]["adminUserSsoPassword"] = env_json_py["universal_authentication"]["universal_password"]
    print("")
    print("Part 10 of 11: vCenter Specs:")
    new_vcf_json_py["vcenterSpec"]["vcenterIp"] = input("Management Domain vCenter IP (default: "+vcf_json_py["vcenterSpec"]["vcenterIp"]+"): ")
    new_vcf_json_py["vcenterSpec"]["vcenterHostname"] = input("Management Domain vCenter Hostname (default: "+vcf_json_py["vcenterSpec"]["vcenterHostname"]+"): ")
    new_vcf_json_py["vcenterSpec"]["licenseFile"] = input("vCenter License (default: "+vcf_json_py["vcenterSpec"]["licenseFile"]+"): ")
    new_vcf_json_py["vcenterSpec"]["rootVcenterPassword"] = env_json_py["universal_authentication"]["universal_password"]
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
    print("Your configuration is stored in a file called "+vcf_json_filename+". Save this configuration for future use.")
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

err = "No arguments found. Instantiating _main_()"
liblog.write_to_logs(err, logfile_name)
_main_()