BIG-IP Terraform Provider
=========================

Overview
----------------------------------
This example uses Terraform to create a private key and a throwaway, self-signed SSL certificate. These resources are in the ``tls.tf`` file. This certificate is then loaded onto the BIG-IP and a clientSSL profile is created on the BIG-IP using this certificate. The resources using the BIG-IP provider are in the ``bigip_config.tf`` file.


How to use this example
----------------------------------
You will need a running BIG-IP, and you will need to know the admin username and password. As per normal Terraform use, run ``terraform init`` to download the required providers and then when running ``terraform apply`` you will be prompted for the username, password, and the IP address of the running BIG-IP that you are targeting.

After trying this example with a self-signed certificate, you should use your own SSL certificate, which you should store securely in a vault. The key can be provided to the BIG-IP provider's `bigip_ssl_key <https://registry.terraform.io/providers/F5Networks/bigip/latest/docs/resources/bigip_ssl_key>`_ resource in PEM format.
