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
    dnslib.configure_tanium_prerequisites()
    dnslib.install_tanium()
    #token = dnslib.get_tanium_token()
    token = ""
    dnslib.get_tanium_token()
    dnslib.change_tanium_password(token)
    sys.exit()

def deploy_vcsa():
    print("Deploy vCenter...")

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

def prompt_user_for_options(user_options):
    prompt = input("Do you want to populate lab environment variables? [y/n] ")
    user_options.append(prompt)
    prompt = input("Do you want to populate vcf bringup variables? [y/n] ")
    user_options.append(prompt)
    prompt = input("Do you want to deploy a DNS server? [y/n] ")
    user_options.append(prompt)
    return user_options

def prompt_vcf_bringup_template():
    print("prompt vcf env...")

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
      prompt_vcf_bringup_template()
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