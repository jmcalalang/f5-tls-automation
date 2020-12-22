Venafi with Application Services 3 (AS3)
========================================

Application Services 3 (AS3) has the ability to pull TLS secrest from an HTTP endpoint with BASIC auth or JSON Web Encryption (JWE). Because Venafi does support BASIC auth, we can use the example below to pull in a TLS secret on application creation.

(Current example is for WAF policies, work in process)

.. literalinclude:: as3_tls_basic.json
  :language: JSON
