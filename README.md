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
# group names should be [location_role]
[do_podman]
do2.example.com
do3.example.com

[yc_ap]
yc1.example.com

[yc_podman]
yc2.ru-central1.internal
yc3.ru-central1.internal

## Location groups
# here you specify location groups
# special configuration options may apply to each location
[do:children]
do_podman

[yc:children]
yc_ap
yc_podman

## Role groups
# here you specify role groups
# roles are performing depending on this groups
[ap:children]
yc_ap

[podman:children]
do_podman
yc_podman
```

### Variables

Group variables are stored in _group_vars_ directory

- _all_: variables applied to all hosts
- _location_: variables applied to specific location

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
[Common]: docs/common.md
