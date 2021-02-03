==============================================
BIG-IP - Letsencrypt with F5 Cloudservices DNS
==============================================

.. note:: Tested with Ansible 2.09
*******
Summary
*******

This ansible role provides following functionality:

* create TLS certificate and key using Letsencrypt as CA
* uses F5 Cloudservices primary DNS offering as validation for domain ownership
* uploads generated certificate and key to a BIG-IP and creates a SSL Client profile with it.


The rolename is: **f5cs_dns_letsencrypt_bigip**

The role can be downloaded from the roles folder here: `Ansible Roles`_.

******************
Steps of the Role:
******************

1. Checks if certificate already exists in certificate folder. If exists skip subsequent certificate creation steps.

2. Create a subdirectory on the ansible host to run and store letsencrypt environment

   - default directory is the ``{{playbook_dir}}/F5letsencrypt``
   - This directory can be changed via variable.

3. Create letsencrypt account ID

   - there is a variable that forces the role to create a new Account ID if desired

4. Create TLS Certificate signing request

   - the csr is stored in the csr subfolder

5. Send API call to Letsencrypt to initiate domain name ownership verification

   - this role uses DNS as verification method.
   - per default it is send to Letsencrypt staging envionment, but a variable will instruct it to send it to Letsencrypt production environment.

6. Create/modify acme-challenge value into F5 Cloudservices primary DNS entry for existing zone record

   - uses an exisiting F5 Cloudservices account with subscription to primary DNS
   - the zone record for the domain name has to exist and be activated prior before the role is run
   - creates or modifies the _acme-challenge dns prefix entry for Letsencrypt verification

7. Send API call to Letsencrypt to finish domain name ownership verification and download certificate and fullchain certificate

   - finishes letsencrypt verification and download certificate, CA certificate and fullchain certificate into the certs subfolder

8. Upload certificate and key into BIG-IP

   - skip this step if ``send_to_bigip`` does not have the value ``on``
   - login credentials with admin rights must be provides

9. Create Client SSL profile in BIG-IP and use uploaded key, certificate and CA

   - installs key, cert and CA cert into BIG-IP and creates a new SSL profile with the cert/key/CAchain

Variables required for the role:
================================

+------------------------+-------------------------------------------+--------------------+
| vars                   | description                               | default values     |
+========================+===========================================+====================+
| f5cs_username:         | Username for F5 Cloudservices account     |                    |
+------------------------+-------------------------------------------+--------------------+
| f5cs_password:         | Password for F5 Cloudservices account     |                    |
+------------------------+-------------------------------------------+--------------------+
| domain_name:           | Domain name for TLS certificate           |                    |
+------------------------+-------------------------------------------+--------------------+
| acme_directory_target: | ``prod`` for Letsencrypt production or    | ``staging``        |
|                        | ``staging`` for Letsencrypt staging       |                    |
+------------------------+-------------------------------------------+--------------------+

Optional variables

+------------------------+-----------------------------------------+----------------------------------+
| vars                   | description                             |  default values                  |
+========================+=========================================+==================================+
| acme_email:            | e-mail address for TSL certificate      | ``myemail@mydomain.com``         |
+------------------------+-----------------------------------------+----------------------------------+
| letsencrypt_dir:       |  directory for Letsencrypt files        |``{{playbook_dir}}/F5letsencrypt``|
+------------------------+-----------------------------------------+----------------------------------+
| new_le_account_key:    | ``true`` or ``false`` - forces role to  | ``false``                        |
|                        | generate a new Letsencrypt account ID   |                                  |
+------------------------+-----------------------------------------+----------------------------------+
| send_to_bigip:         | ``on`` to send cert/key to BIG-IP       |  ``on``                          |
|                        | any other value skipps importing of     |                                  |
|                        | cert/key into BIG-IP. Good for testing  |                                  |
+------------------------+-----------------------------------------+----------------------------------+


Example playbooks
=================

Following are some examples how playbooks that use the role could look like.

Use case 1: Upload into single BIG-IP
-------------------------------------
This playbook assumes the roles folder location is under the playbook folder.
Please adjust to ansible host environment.

.. literalinclude :: example_playbook.yml
   :language: yaml

This example playbook uploads the certificate and key into a single BIG-IP.
BIG-IP admins can perform a config sync between BIG-IP devices to sync the new cert/key and Client SSL profile.

Use case 2: Upload into multiple BIG-IP
---------------------------------------

It is possible to upload the cert/key pair to multiple BIG-IP instances as well.

The login credentials for multiple BIG-IP's are stored in the ``host_vars/`` folder.
Each BIG-IP has an individual file with its own provider variables.

Therefore there are no provider variables in the playbook.

To upload the key to multiple BIG-IP instances perform followong steps:

1. Change the playbook ``hosts: localhost`` value to a var group e.g.  ``hosts: bigip_group``

.. literalinclude :: example_playbook_multiple_bigip.yml
   :language: yaml



2. Create a var group with the same name in the hosts :file:

.. literalinclude :: hosts_multiple
   :language: yaml`

3. Create a host_vars folder and add vars file for each BIG-IP in the "bigip_group".
Use following content for each file and adjust the var values accordingly

.. literalinclude :: example_bigip
   :language: yaml`

Example Run command:
====================

Here some examples, how to run the role.
The login parameters for F5 Cloudservices can be:

a. handed over as variables during the call or
b. can be part of the playbook as shown in the playbook examples.

Letsencrypt staging
-------------------

Example run command for Letsencrypt staging API environment.
Letsencrypt staging environment **does not** create valid TLS certificates. It can be used for testing and verification.

This is the default setting of the role. This is done to prevent the user to use all

``ansible-playbook example_playbook.yml  -e "domain_name=<www.mydomain.com>"``

Letsencrypt production
----------------------

Example run command for Letsencrypt production API environment. This command creates valid TLS certificates:

``ansible-playbook example_playbook.yml  -e "domain_name=<www.mydomain.com>" -e "acme_email=certadmin@mydomain.com" -e "acme_directory_target=prod"``

use role without uploading to BIG-IP
------------------------------------

If it is not desired to upload the cert/kei into BIG-IP use the ``send_to_bigip=off`` flag

``ansible-playbook example_playbook.yml  -e "domain_name=<www.mydomain.com>" -e "acme_email=certadmin@mydomain.com" -e "acme_directory_target=prod" -e "send_to_bigip=off"``

This will create the folder structure. Per default a ``F5letsencrypt`` folder is created under the playbook directory. Subfolders for **keys** , **certs** and **csrs** are created.

change folder for letsencrypt certificate/keys
----------------------------------------------

To change the location of the letsencrypt folder structure, use the ``letsencrypt_dir`` variable.

``ansible-playbook example_playbook.yml  -e "domain_name=<www.mydomain.com>" -e "acme_email=certadmin@mydomain.com"  -e "letsencrypt_dir=/var/temp/letsencrypt"``

workaround Letsencrypt ratelimiting
-----------------------------------

Letsencrypt limits the number of requests a single account key can send in a given time interval. I found it usefull to have a limited workaround to extend the rate li8mit during tests and development.
One limiting factor is the account key. With following variable, the role will generate a new Account key and allow to moire testing, before IP rate limiting of letsencrpt kick in:

``ansible-playbook example_playbook.yml  -e "domain_name=<www.mydomain.com>" -e "acme_email=certadmin@mydomain.com" -e "acme_directory_target=prod" -e "new_le_account_key=true"``

.. warning:: This role will create a folder structure to store letsencrypt account key, certificate, key, CA certificate and csr.

Example Ansible environment:
============================

An example ansible environment can be here: `Ansible Environment`_


.. _`Ansible Roles`: https://github.com/jmcalalang/f5-tls-automation/tree/main/code/letsencrypt/roles

.. _`Ansible Environment`: https://github.com/jmcalalang/f5-tls-automation/tree/main/code/letsencrypt/example_ansible_env
