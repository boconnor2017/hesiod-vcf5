# Hesiod VCF5
Uses [Project Hesiod](https://github.com/boconnor2017/hesiod), a Photon based approach to initiate and launch a VCF 5 bringup ready environment. The purpose of this project is to facilitate hands on experience with the VCF Bringup using a nested environment. There are two goals with this project:

| Goal | Description |
|------|-------------|
| Accelerate the Prerequisites Process | This project uses a CLI driven prompt to configure 2x backend JSON files. The prompt asks for critical VCF inputs to make the process as similar as if the user were deploying a standard OVA. **Optional:** this project comes with a DNS server. |
| Reduce Hardware Resource Requirements | This project can run on a **SINGLE** ESXi host. All scripting in this repository interacts with the ESXi host directly, thus saving resources. | 

# Prerequisites
The following physical equipment is **required** to run hesiod-vcf5:

| Requirement | Description |
|-------------|-------------|
| Physical Network | ability to provision multiple /24 VLANs: Management, VLAN, VSAN, NSX |
| Physical ESXi | at least 1x physical server with 8 logical processors, 125GB Memory, and 800GB storage |

The following binaries are **required** to run hesiod-vcf5:

| Requirement | Description |
|-------------|-------------|
| PhotonOS OVA | version 5.0 recommended (download from [here](https://vmware.github.io/photon/).) |
| Nested ESXi Appliance | version 8.0U3 (the easiest approach is to download from [William Lam's blog](https://williamlam.com/nested-virtualization/nested-esxi-virtual-appliance)) |
| VCF Cloud Builder Appliance | version 5.2 |
| 1x vSphere License | Minimum: 32 cores |
| 1x vSAN License | No minimums |
| 1x vCenter License | No minimums |
| 1x NSX License | No minimums |

**Optional:** for more advanced automation development capabilities with Python, Terraform, Ansible, etc you can use hesiod-vcf to deploy a vCenter Server. Note that more physical resources may be required to support this. 

|Requirement | Description |
|------------|-------------|
| VMware vCenter Server Appliance | VMware-VCSA-all-8.0.3-24022515.iso |

# Quick Start
Deploy Photon OS OVA to the physical server. Follow the steps in the [Hesiod Photon OS Quick Start](https://github.com/boconnor2017/hesiod/blob/main/photon/readme.md) readme file. 

Next, install OVFTool by following the steps in the [Hesiod Install OVFTool on Photon OS](https://github.com/boconnor2017/hesiod/tree/main/ovftool) process.

Recommended: run these scripts as root
```
sudo su
```
```
cd /usr/local/
```
```
git clone https://github.com/boconnor2017/hesiod-vcf5
```
```
cp -r hesiod/python/ hesiod-vcf5/hesiod
```
```
cd hesiod-vcf5/
```

## This is my first time running this script...
If you need a DNS server, spin up a new PhotonOS VM, repeat the quickstart steps above, and run hesiod-vcf with the `-dns` parameter:
```
python3 hesiod-vcf5.py -dns
```

If you want to be prompted to edit lab variables use the `-lev` parameter to create a lab.json file:
```
python3 hesiod-vcf5.py -lev
```
```
mv lab.json /usr/local/drop/lab.json
```

If you want to be prompted to edit VCF variables use the `-vcf` parameter to create a vcf.json file:
```
python3 hesiod-vcf5.py -vcf
```
```
mv vcf.json /usr/local/drop/vcf.json
```

## I'm a pro already, let's get on with it...
If you need to copy your `-lev` config
```
rm json/lab*
```
```
cp /usr/local/drop/lab.json json/lab_environment.json
```

If you need to copy your `-vcf` config
```
rm json/vcf5*
```
```
cp /usr/local/drop/vcf.json json/vcf5_bringup_template.json
```

If your `-lev` config file, your `-vcf` config file, and your VCF dns entries are ready to rock and roll:
```
python3 hesiod-vcf5.py 
```

## I'm a VCF developer, I don't need everything...
If you want to deploy a vCenter server, spin up a new PhotonOS VM and run hesiod-vcf with the `-vcs` parameter **after** you've completed these steps:
1. lab_environment.json parameters are configured
2. DNS entries are completed
3. The vCenter ISO is mounted to the PhotonOS VM
```
python3 hesiod-vcf5.py -vcs
```

If you want to deploy a single nested ESXi server, spin up a new PhotonOS VM, repeat the quickstart steps above, and run hesiod-vcf with the `-esx` parameter **after** you've completed these steps:
1. Download Nested ESXi OVA to `/usr/local/drop/`
```
python3 hesiod-vcf5.py -esx
```