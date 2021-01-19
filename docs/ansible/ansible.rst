BIG-IP Ansible Modules
======================

This task is designed to show pulling a certificate from a URL endpoint and publishing this into a BIG-IP. URL endpoint examples are great for their reusability. Most TLS management solutions will have an API endpoint which this module could consume hold in a fact and publish.

- Pull Certificate from URL
- Store Certificate in location
- Upload Certificate to BIG-IP
- Create SSL Profile on BIG-IP
- Delete Certicates from playbook path

Modify the main.yml file for correct variables, tested with Ansible 2.10

**ansible-playbook main.yml**
