===============
Oracle JRE Role
===============

Tasks
=====

* Installs Oracle JRE from Debian package. Deb-package download link must be provided.
  Use ``java-package`` to build your own:

  .. code:: bash

      $ sudo apt-get install java-package
      $ wget http://java.com/path/to/jre.tar.gz
      $ make-jpkg jre.tar.gz

* Installs java native access.

Variables
=========

+-----------------------+----------+--------------------------+--------------------------------+
| Variable              | Required | Default                  | Description                    |
+=======================+==========+==========================+================================+
| ``jre_package_name``  | no       | ``oracle-java7-jre.deb`` | JRE package name.              |
+-----------------------+----------+--------------------------+--------------------------------+
| ``jre_download_link`` | yes      |                          | JRE deb-package download link. |
+-----------------------+----------+--------------------------+--------------------------------+
