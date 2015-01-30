===============
Oracle JRE Role
===============

Tasks
=====

* Installs Oracle JRE from apt repository. Apt repository must be provided.
  Use ``java-package`` to build your own package:

  .. code:: bash

      $ sudo apt-get install java-package
      $ wget http://java.com/path/to/jre.tar.gz
      $ make-jpkg jre.tar.gz

  Then you can publish this package to your private apt repo (e.g. using aptly_).

.. _aptly: http://www.aptly.info/tutorial/repo/

* Installs java native access.


Variables
=========

+-----------------------+----------+----------------------+-------------------------------------+
| Variable              | Required | Default              | Description                         |
+=======================+==========+======================+=====================================+
| ``jre_package_name``  | no       | ``oracle-java7-jre`` | JRE package name.                   |
+-----------------------+----------+----------------------+-------------------------------------+
| ``jre_debian_repo``   | yes      |                      | Apt repo containing JRE package     |
+-----------------------+----------+----------------------+-------------------------------------+
| ``jre_pgp_keyserver`` | yes      |                      | PGP Keyserver for JRE apt repo key. |
+-----------------------+----------+----------------------+-------------------------------------+
| ``jre_pgp_key_id``    | yes      |                      | PGP key id for JRE apt repo.        |
+-----------------------+----------+----------------------+-------------------------------------+
