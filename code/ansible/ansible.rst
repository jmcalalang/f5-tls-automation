BIG-IP Ansible Modules
======================

This task is designed to show pulling Certificates/Keys from a URL endpoint and publishing this into a BIG-IP. URL endpoint examples are remarkable for their reusability. Most TLS management solutions will have an API endpoint, which this module can consume.

.. note:: If you dont want to pull the Certificates/Keys from a URL, you can remove that part of the task and have them local to the playbook.

Steps of the task:

- Pull Certificates/Key from URL
- Store Certificates/Key in location
- Upload Certificates/Key to BIG-IP
- Create SSL Profile on BIG-IP
- Delete Certificates/Key from playbook path

.. warning:: This task will delete files, its designed this way, so Certificates/Keys are not left residually

Clone the repository, or copy main.yml below, modify the task for correct variables.

.. note:: Tested with Ansible 2.10

**ansible-playbook main.yml**

.. literalinclude :: main.yml
   :language: yaml
