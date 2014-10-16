#!/bin/bash

ansible-playbook bootstrap.yml -k -e host=${1}
