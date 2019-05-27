Python3
=========

[![Build Status](https://travis-ci.org/lesfurets/ansible-role-python3.svg?branch=master)](https://travis-ci.org/lesfurets/ansible-role-python3)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Ansible Galaxy: lesfurets.python3](https://img.shields.io/badge/galaxy-lesfurets.python3-blueviolet.svg)](https://galaxy.ansible.com/lesfurets/python3)

Ansible role to install python3 from system package

## Requirements

None

## Role Variables

None, this role simply install python3

## Dependencies

Role **lesfurets.epel** is used for RedHat/CentOS.

## Example Playbook

    - hosts: servers
      roles:
         - lesfurets.python3

## License

Licensed unter the GPLv3 License. See LICENSE file for details.
