=================
ansible-playbooks
=================

Collection of ansible_ playbooks for Debian Wheezy.

.. _ansible: http://docs.ansible.com/


Roles
=====

* `Common`_
* `Cassandra`_
* `Nginx`_
* `Oracle JRE`_
* `Postgresql`_
* `Redis`_
* `Sentry`_


Usage
=====

Playbooks are organized according to `Ansible Best Practices`_.

.. _Ansible Best Practices: http://docs.ansible.com/playbooks_best_practices.html


Inventory file
--------------

To start using playbooks, first of all you need to create ansible inventory file:

.. code:: ini

    # /etc/ansible/hosts

    ## Servers
    # here you define your hosts
    # group names should be [location_name-role_name]

    [hetzner-webservers]
    www01.example.com
    www02.example.com

    [aws-webservers]
    www03.example.com

    [aws-postgresql_servers]
    db01.example.com

    ## Location groups
    # here you specify location groups
    # special configuration options may apply to each location
    [hetzner:children]
    hetzner-webservers

    [aws:children]
    aws-webservers
    aws-postgresql_servers

    ## Role groups
    # here you specify role groups
    # roles are performing depending on this groups
    [webservers:children]
    hetzner-webservers
    aws-webservers

    [postgresql_servers:children]
    aws-postgresql_servers


Variables
---------

Group variables are stored in *group_vars* directory

* *all* - variables applied to all hosts
* *location_name (eg. hetzner, aws)* - variables applied to specific location

You can also set variables for specific host by creating file with name matching servers' hostname in *host_vars* directory.


Role groups
-----------

* all

  - perform Common_ role

* cassandra_nodes

  - perform `Oracle JRE`_ role
  - perform Cassandra_ role

* postgresql_servers

  - perform Postgresql_ role
  - open TCP port 5432 in iptables for ``postgresql_accept`` and ``postgresql_accept6`` lists

* redis_servers

  - perform Redis_ role

* sentry_servers

  - perform Sentry_ role

* webservers
  - perform Nginx_ role
  - open TCP ports 80,443 in iptables

Run playbooks
-------------

To run playbook for all servers:

.. code:: bash

    $ ansible-playbook site.yml

Also you can run playbook on speciafied role group:

+------------------------+--------------------+------------+
| Playbook               | Groups             | Roles      |
+=============================================+============+
| all_servers.yml        | all                | common     |
+------------------------+--------------------+------------+
| cassandra_nodes.yml    | cassandra_nodes    | cassandra  |
+------------------------+--------------------+------------+
| oracle_jre_hosts.yml   | cassandra_nodes    | oracle_jre |
+------------------------+--------------------+------------+
| postgresql_servers.yml | postgresql_servers | postgresql |
+------------------------+--------------------+------------+
| redis_servers.yml      | redis_servers      | redis      |
+------------------------+--------------------+------------+
| sentry_servers.yml     | sentry_servers     | sentry     |
+------------------------+--------------------+------------+
| webservers.yml         | webservers         | nginx      |
+------------------------+--------------------+------------+


Bootstrapping a server
======================

.. code:: bash

    $ ./bootstrap.sh server.example.com

Bootstrap playbook installs dependencies for ansible (python, python-apt and pycurl), sets hostname and performs Common_ role on specified server. If hostname and/or timezone changes server will be rebooted.


Using playbooks with vagrant_
=============================

.. _vagrant: https://www.vagrantup.com/

Vagrant provisioning
--------------------

Add following lines to ``ansible.cfg``:

.. code:: ini

    roles_path = /path/to/ansible-playbooks/playbooks/roles
    filter_plugins = /path/to/ansible-playbooks/playbooks/filter_plugins

Create ``Vagrantfile`` in your project root:

.. code:: ruby

    VAGRANTFILE_API_VERSION = "2"

    Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
        config.vm.box = "priver/wheezy-amd64"

        # config.vm.network "forwarded_port", guest: 80, host: 8080
        # config.vm.synced_folder "../data", "/vagrant_data"

        config.vm.provision "ansible" do |ansible|
            ansible.groups = {
                "postgresql_servers" => ["default"]
            }

            ansible.playbook = "provisioning/playbook.yml"
        end
    end

Then create ``provisioning/playbook.yml`` like this:

.. code:: yaml

    ---
    - hosts: default
      remote_user: vagrant
      sudo: yes

      vars:
        users:
          - user:
              name: vagrant
              password: "$6$ERfXCVxk$mmdpfeit6dZMQrqRxrE2/LNKGKnIp47UuYzJPF3RvOtpT3jgVDF5hHnA1r0pQYg6bwd4pkQlm9yQSa.OdZQtK1"
              email_alias: vagrant
              uid: 1000
              gecos: vagrant
              authorized_keys:
                - ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
            groups: adm

        nameservers:
          - 10.0.2.3

        sysctl_additional:
          - { name: vm.swappiness, value: 0 }

        ssh_accept:
          - 10.0.2.2

        postgresql_accept:
          - 10.0.2.2/32

        postgresql_databases:
          - { name: mydb, password: mypasswd }

        mailname: vagrant

      roles:
        - postgresql

Now you can run your virtual machine with ``vagrant up`` command.


Creating a base box
-------------------

You can create Debian Wheezy Vagrant box and apply Common_ role to it. All the variables are stored directly in the playbook file (``vagrant_box.yml``), you can change them before role performance. You need to install debian Wheezy on VirtualBox VM and run:

.. code:: bash

    $ ansible-playbook vagrant_box.yml -i vagrant_hosts
    $ vagrant package --base <VM_name>

Or you can check out `my box`_ at Atlas.

.. _my box: https://atlas.hashicorp.com/priver/boxes/wheezy-amd64

.. _Common: docs/common.rst
.. _Cassandra: docs/cassandra.rst
.. _Nginx: docs/nginx.rst
.. _Oracle JRE: docs/oracle_jre.rst
.. _Postgresql: docs/postgresql.rst
.. _Redis: docs/redis.rst
.. _Sentry: docs/sentry.rst
