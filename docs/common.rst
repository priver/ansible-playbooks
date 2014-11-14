===========
Common Role
===========

Tasks
=====

* gai

  - Sets precedence of IPv6 below IPv4.

* packages

  - Sets Debian apt mirrors.
  - Configures unattended-upgrades of Debian Security repo.
  - Install essential packages.

* locale

  - Generates locales.
  - Sets default locale.
  - Configures keyboard.

* dns

  - Installs and configures unbound for local resolver cache.

* time

  - Sets timezone; if timezone changes restarts time critical services (cron, rsyslog), but you should consider rebooting your server.
  - Installs and configures NTP client.

* sudo

  - Configures passwordless sudo for memebers of *adm* group.

* users

  - Create users.
  - If user has dotfiles, then task will clone them to ``.dotfiles`` directory and run ``make install``.
  - Delete authorized keys for all unknown users.

* ssh

  - Configures OpenSSH server.

* mail

  - If ``smtp_smarthost`` is defined configure exim4 to send outgoing emails though it.
  - Sets user email aliases.

* sysctl

  - Sets sysctl parameters.

* iptables

  - Configures iptables rules.


Variables
=========

+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| Variable                        | Required | Default                   | Description                                                                 |
+=================================+==========+===========================+=============================================================================+
| ``apt_repos``                   | no       | ``[]``                    | Location-specific list of Debian apt repos.                                 |
|                                 |          |                           | These repos (and corresponding deb-src) will always be added as a backup::  |
|                                 |          |                           |                                                                             |
|                                 |          |                           |   deb http://http.debian.net/debian/ wheezy main non-free contrib           |
|                                 |          |                           |   deb http://http.debian.net/debian wheezy-updates main                     |
|                                 |          |                           |   deb http://http.debian.net/debian/ wheezy-backports main non-free contrib |
|                                 |          |                           |   deb http://security.debian.org/ wheezy/updates  main contrib non-free     |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``locales``                     | no       | ``[en_US.UTF-8 UTF-8]``   | List of genereated locales. First will be default.                          |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``keyboard_layouts``            | no       | ``[us]``                  | List of keyboard layouts.                                                   |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``nameservers``                 | no       | ::                        | List of nameservers.                                                        |
|                                 |          |                           |                                                                             |
|                                 |          |   - 8.8.8.8               |                                                                             |
|                                 |          |   - 8.8.4.4               |                                                                             |
|                                 |          |   - 2001:4860:4860::8888  |                                                                             |
|                                 |          |   - 2001:4860:4860::8844  |                                                                             |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``unbound_extended_statistics`` | no       | ``no``                    | Should unbound log extended statistics. Not recommended for production.     |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``timezone``                    | no       | ``UTC``                   | Timezone. Changing this setting require reboot.                             |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``ntp_servers``                 | no       | ::                        | List of NTP servers.                                                        |
|                                 |          |                           |                                                                             |
|                                 |          |   - 0.debian.pool.ntp.org |                                                                             |
|                                 |          |   - 1.debian.pool.ntp.org |                                                                             |
|                                 |          |   - 2.debian.pool.ntp.org |                                                                             |
|                                 |          |   - 3.debian.pool.ntp.org |                                                                             |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``users``                       | no       | ``[]``                    | See `Users variable`_.                                                      |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``sysctl_additional``           | no       | ``[]``                    | List of sysctl paramters in ``{ name: vm.swappiness, value: 0 }`` format.   |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``mailname``                    | no       | *domain name*             | ``/etc/mailname``                                                           |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``smtp_smarthost``              | no       |                           | SMTP smarthost for outgoing emails (eg. Mailgun).                           |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``smtp_smarthost_port``         | no       |                           | SMTP smarthost port (required if ``smtp_smarthost`` is defined).            |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``smtp_smarthost_login``        | no       |                           | SMTP smarthost login (required if ``smtp_smarthost`` is defined).           |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+
| ``smtp_smarthost_password``     | no       |                           | SMTP smarthost password (required if ``smtp_smarthost`` is defined).        |
+---------------------------------+----------+---------------------------+-----------------------------------------------------------------------------+


Users variable
--------------

I recommend following data structure. Define ``user_list`` variable containing all users in ``group_vars\all`` file:

.. code:: yaml

    user_list:
      vagrant:
        name: vagrant
        password: "$6$ERfXCVxk$mmdpfeit6dZMQrqRxrE2/LNKGKnIp47UuYzJPF3RvOtpT3jgVDF5hHnA1r0pQYg6bwd4pkQlm9yQSa.OdZQtK1"
        email_alias: vagrant
        uid: 1000
        gecos: vagrant
        authorized_keys:
          - ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
      someuser:
        name: someuser
        email_alias: someuser
        uid: 2001
        gecos: Some User
        authorized_keys:
          - ssh-rsa PUBKEY
        dotfiles: "https://github.com/someuser/dotfiles.git"

Then for specific group or host define ``users`` variable containg users from ``user_list``:

.. code:: yaml

    users:
      - { user: "{{ user_list.someuser }}", groups: adm }
