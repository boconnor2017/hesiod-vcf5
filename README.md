# Hesiod VCF5
Uses [Project Hesiod](https://github.com/boconnor2017/hesiod) to initiate and launch an immutable VCF5 environment on [Photon OS](https://vmware.github.io/photon/).

# Prerequisites
The following prerequisites are required to run hesiod-vcf5:

| Requirement | Description |
|-------------|-------------|
| Physical Network | ability to provision multiple /24 VLANs |
| Physical ESXi | at least 1x physical server with 8 logical processors, 125GB Memory, and 800GB storage |
| PhotonOS OVA | version 5.0 recommended |
| VMware vCenter Server Appliance | VMware-VCSA-all-8.0.3-24022515.iso |
| Nested ESXi Appliance | version 8.0U3 (the easiest approach is to download from [William Lam's blog](https://williamlam.com/nested-virtualization/nested-esxi-virtual-appliance)) |
| VCF Cloud Builder Appliance | version 5.2 |

# Quick Start
Deploy Photon OS OVA to the physical server. Follow the steps in the [Hesiod Photon OS Quick Start](https://github.com/boconnor2017/hesiod/blob/main/photon/readme.md) readme file. 

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
If your prerequisites (config files, vcenter, and dns) are ready to rock and roll:
```
python3 hesiod-vcf5.py 
```
If you want to be prompted to edit lab variables use the `-lev` parameter:
```
python3 hesiod-vcf5.py -lev
```
If you want to be prompted to edit VCF variables use the `-vcf` parameter
```
python3 hesiod-vcf5.py -vcf
```

## Deploy a DNS Server
If you want to deploy a DNS server, spin up a new PhotonOS VM and run hesiod-vcf with the `-dns` parameter:
```
python3 hesiod-vcf5.py -dns
```

## Deploy a vCenter Server
If you want to deploy a vCenter server, spin up a new PhotonOS VM and run hesiod-vcf with the `-vcs` parameter:
```
python3 hesiod-vcf5.py -vcs
```