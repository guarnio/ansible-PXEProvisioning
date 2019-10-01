ansible-PXEProvisioning
=========

PXE provisioning of VM using libvirt, based on isc-dhcpd, bind9 and tftp for PXE.

IMPORTANT NOTE:
replace <username>, <password> and <public key> with your own in templates/ks/\*.ks files

Requirements
------------

Tested with Ansible 2.4 on RHEL 7.4 hipervisor

Role Variables
--------------


```yaml
bind_fw: "/var/named/example.com.local"
bind_rev: "/var/named/db.124.168.192"
tftp_folder: "/var/lib/tftpboot/pxelinux/pxelinux.cfg/"
dns: localhost
hipervisor: localhost
tftp_server: localhost
```

dictionary below is also needed during the setup of the PXE environment:

```yaml
managed_domains:
  - dns_domain: example.com
    network: 192.168.124.0
    netmask: 255.255.255.0
    gateway: 192.168.124.1
    dns: 192.168.124.1
    next_server: 192.168.124.1
    dhcp_range:
        start: 192.168.124.200
        end: 192.168.124.209
    dhcp_boot_range:
        start: 192.168.124.210
        end: 192.168.124.219
  - dns_domain: iaas.example.com
    network: 192.168.125.0
    netmask: 255.255.255.0
    gateway: 192.168.125.1
    dns: 192.168.125.1
    next_server: 192.168.125.1
    dhcp_range:
        start: 192.168.125.200
        end: 192.168.125.209
    dhcp_boot_range:
        start: 192.168.125.210
        end: 192.168.125.219

iso_images:
  - cd: "/srv/rhel-server-7.6-x86_64-dvd.iso"
    path: "/var/www/html/rhel/7.6/server/x86_64/os"
    desc: "RHEL-7.6"
  - cd: "/srv/rhel-server-7.4-x86_64-dvd.iso"
    path: "/var/www/html/rhel/7.4/server/x86_64/os"
    desc: "RHEL-7.4"
  - cd: "/srv/rhel-server-7.3-x86_64-dvd.iso"
    path: "/var/www/html/rhel/7.3/server/x86_64/os"
    desc: "RHEL-7.3"


boot_message: "BCGAudio PXE Provisioning Server"
install_packages: true
```

VM could be personalized overwriting the default settings below

```yaml
ram: 2048
disks:
  - size: 24
    pool: default
os_type: linux
# to get a list of supported vaules for os_variant run "osinfo-query os"
os_variant: rhel7
net: default
```


Dependencies
------------

N/A

Example Playbook
----------------


```yaml
- name: add vm to pxe environment
  hosts: "{{ variable_host | default('dummy') }}"
  gather_facts: False
  vars:
    bind_fw: "/var/named/example.com.local"
    bind_rev: "/var/named/db.124.168.192"
    tftp_folder: "/var/lib/tftpboot/pxelinux/pxelinux.cfg/"
    dns: localhost
    hipervisor: localhost
    tftp_server: localhost
  vars_files:
    - environmental-variables/main.yaml
  roles:
    - ansible-PXEProvisioning
```

"environmental-variables/main.yaml" should at least contain the dictionary shown on "Roles Variables" section.


License
-------

BSD

Author Information
------------------

Marco Guarnieri  
mguarnieri@outlook.es  
January '18  
