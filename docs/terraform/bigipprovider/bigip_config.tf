
resource "bigip_ssl_certificate" "test-cert" {
  name      = "servercert.crt"
  content   = tls_self_signed_cert.example.cert_pem
  partition = "Common"
}

resource "bigip_ssl_key" "test-key" {
  name      = "serverkey.key"
  content   = tls_private_key.example.private_key_pem
  partition = "Common"
}

resource "bigip_ltm_profile_client_ssl" "test-ClientSsl" {
  name          = "/Common/test-ClientSsl"
  defaults_from = "/Common/clientssl"
  #authenticate  = "always"
  ciphers = "DEFAULT"
  cert    = "/Common/servercert.crt"
  key     = "/Common/serverkey.key"
}
