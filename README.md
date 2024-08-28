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
cd /usr/local/hesiod/
```
```
git clone https://github.com/boconnor2017/hesiod-vcf5
```
```
cd hesiod-vcf5/
```
```
python3 hesiod-vcf5.py
```