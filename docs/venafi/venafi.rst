Venafi Ansible Modules
======================

This task is designed to show pulling a certificate from a Venfai certificate mananagement solution and publishing into a BIG-IP. Venfai solutions offer BASIC auth as a mechanism to access the solution.

**Tested with Ansible 2.10**

- Pull Certificates/Key from Venafi API
- Store Certificates/Key in location
- Upload Certificates/Key to BIG-IP
- Create SSL Profile on BIG-IP
- Delete Certificates/Key from playbook path

Clone the repository, or copy main.yml below, modify the task for correct variables.

**ansible-playbook main.yml**

.. literalinclude :: main.yml
   :language: yaml
