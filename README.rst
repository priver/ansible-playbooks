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

* cassandra_nodes

  - perform Cassandra_ role

* postgresql_servers

  - perform Postgresql_ role
  - open TCP port 5432 in iptables for postgresql_accept and postgresql_accept6 lists

* webservers

  - open TCP ports 80,443 in iptables

Run a playbooks
---------------

To run playbook for all servers:

.. code:: bash

    $ ansible-playbook site.yml

Also you can run playbook on speciafied role group:

* cassandra_nodes.yml
* postgresql_servers.yml


Bootstrapping a server
======================

.. code:: bash

    $ ./bootstrap.sh server.example.com

Bootstrap playbook installs dependencies for ansible (python, python-apt and pycurl), sets hostname and performs Common_ role on specified server. If hostname and/or timezone changes server will be rebooted.


Using playbooks with vagrant
============================

Vagrant provisioning
--------------------

*TODO*


Creating a base box
-------------------

You can create Debian Wheezy Vagrant box and apply Common_ role to it. All the variables are stored directly in the playbook file (``vagrant_box.yml``), you can change them before role performance. You need to install debian Wheezy on VirtualBox VM and run:

.. code:: bash

    $ ansible-playbook vagrant_box.yml -i vagrant_hosts
    $ vagrant package --base <VM_name>

Or you can checkout `my box`_ at Vagrant Cloud.

.. _my box: https://vagrantcloud.com/priver/boxes/wheezy-amd64

.. _Common: docs/common.rst
.. _Cassandra: docs/cassandra.rst
.. _Nginx: docs/nginx.rst
.. _Oracle JRE: docs/oracle_jre.rst
.. _Postgresql: docs/postgresql.rst
