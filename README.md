# ansible-playbooks

Collection of [ansible] playbooks for Debian Bookworm.

## Roles

- [Common]

## Usage

Playbooks are organized according to [Sample Ansible setup].

### Inventory file

To start using playbooks, first of all you need to create ansible inventory file:

```ini
# inventories/hosts

## Servers
# here you define your hosts
# group names should be [location_name-role_name]
[do-docker]
do1.example.com
do2.example.com
do3.example.com

[yc-docker]
yc1.example.com
yc2.example.com
yc3.example.com

## Location groups
# here you specify location groups
# special configuration options may apply to each location
[do:children]
do-docker

[yc:children]
yc-docker

## Role groups
# here you specify role groups
# roles are performing depending on this groups
[docker:children]
do-docker
yc-docker
```

### Variables

Group variables are stored in _group_vars_ directory

- _all_: variables applied to all hosts
- _location_name_: variables applied to specific location

You can also set variables for specific host by creating file with name matching servers' hostname
in _host_vars_ directory.

### Role groups

- all
  - perform [Common] role

### Run playbooks

To run playbook for all servers:

```sh
ansible-playbook site.yml
```

[ansible]: http://docs.ansible.com
[Sample Ansible setup]: https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html
[Common]: docs/common.rst
