# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import VCF libraries
from lib import deploy_dns as dnslib
from lib import deploy_vcenter as vcslib
from lib import deploy_nested_esxi_hosts as esxlib
from lib import prompts as promptlib
from lib import markdown as mdlib

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
    print("-validate-vcf  option to create a markdown file of a vcf.json configuration.")
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

def match_valvcs(args):
    if '-validate-vcf' in args:
        return True

def validate_vcf(vcf_json_py):
    script = mdlib.get_validate_vcf_md_script(vcf_json_py)
    md_script_name = "vcf-validation.md" #hardcoded
    mdlib.write_cmd_to_script_file(script, md_script_name)

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
      promptlib.prompt_lab_environment_config(env_json_py)
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_vcf(sys.argv)
  if match_found :
      err = "    -vcf found. Initiating vcf bringup prompts."
      liblog.write_to_logs(err, logfile_name)
      promptlib.prompt_vcf_bringup_template(vcf_json_py, env_json_py)
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
      err = "    -esx found. Initiating ESXi deployment."
      liblog.write_to_logs(err, logfile_name)
      deploy_esx()
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_valvcs(sys.argv)
  if match_found :
      err = "    -validate-vcf found. Initiating validation of VCF configuration."
      liblog.write_to_logs(err, logfile_name)
      validate_vcf(vcf_json_py)
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

err = "No arguments found. Instantiating _main_()"
liblog.write_to_logs(err, logfile_name)
_main_()