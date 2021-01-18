Introduction
============

This Project is a derivative of F5s *Automate One Thing* workshop. Its goal is to build a central example repository for Secrets (TLS) management on F5 products (BIG-IP, NGINX, F5 Cloud Services, etc.). Within the solution, you will find examples of TLS automation for different integrations across different platforms.

(SSL_offloading_) is the process of removing the SSL-based encryption from incoming traffic to relieve a web server of the processing burden of decrypting or encrypting traffic sent via SSL. The processing is offloaded to a separate device designed specifically for SSL acceleration or SSL termination.

|image1|

The examples contained within this repository are designed to be run from their respective folder structure. To see the solution work, clone this repository, navigate to the example you would like to try, and use the instructions provided.

Example:

BIG-IP with Ansible

- clone repository
- navigate to /docs/ansible
- follow instructions


.. |image1| image:: images/image1.png

.. _SSL_offloading: https://www.f5.com/services/resources/glossary/ssl-offloading
