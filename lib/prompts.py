import sys 
from hesiod import lib_json as libjson

def prompt_vcf_bringup_template(vcf_json_py, env_json_py):
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

def prompt_lab_environment_config(env_json_py):
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
        new_env_json_py["physical_server"][i]["deploy_vms_to_this_network"] = input("Network where you want to deploy VMs (example: VM Network): ")
        new_env_json_py["physical_server"][i]["deploy_vms_to_this_datastore"] = input("Datastore where you want to deploy VMs (example: datastore1): ")
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
    print("** For development teams who need a vCenter. **")
    new_env_json_py["vcenter_server"]["vm_name"] = input("Name of the VCSA virtual machine: ")
    new_env_json_py["vcenter_server"]["fqdn"] = input("FQDN of the vCenter Server: ")
    new_env_json_py["vcenter_server"]["ip"] = input("IP Address of the vCenter Server: ")
    number_of_networks = len(env_json_py["physical_network"])
    vcenter_network = input("Which physical network do you want to use to configure this vCenter? (Select: 0-"+str(number_of_networks)+") ")
    new_env_json_py["vcenter_server"]["deploy_to_physical_network"] = int(vcenter_network)
    number_of_servers = len(env_json_py["physical_server"])
    if (number_of_servers-1) == 0:
        vcenter_server = 0
    else:
        vcenter_server = input("Which physical server do you want to use to deploy this vCenter? (Select: 0-"+str(number_of_servers)+") ")
    new_env_json_py["vcenter_server"]["deploy_to_physical_host"] = int(vcenter_server)
    print("")
    print("Part 7 of 7 - Nested ESXi.")
    print("** The specs for the nested ESXi hosts (you need these for your VCF environment). **")
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
        if (number_of_servers-1) == 0:
            deploy_to_esxi_server = 0
        else:
            deploy_to_esxi_server = input("Which physical host do you want to use to deploy this VM? (Select: 0-"+str(number_of_servers)+") ")
        new_env_json_py["nested_esxi_servers"]["host_specs"][i]["deploy_to_physical_host"] = int(deploy_to_esxi_server)
        deploy_to_physical_network = deploy_to_esxi_server #Hardcoded
        new_env_json_py["nested_esxi_servers"]["host_specs"][i]["deploy_to_physical_network"] = int(deploy_to_physical_network)
        i = i+1
    lab_json_filename = "lab.json"
    libjson.dump_json_to_file(new_env_json_py, lab_json_filename)
    print("")
    print("Completed!")
    print("Your configuration is stored in a file called "+lab_json_filename+".")
    print("To save this configuration for future use, run: mv lab.json /usr/local/drop/lab.json")
    sys.exit()
