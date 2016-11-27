# -*- coding: utf-8 -*-

SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
EXC_NS = 'http://www.w3.org/2001/10/xml-exc-c14n#'
DS_NS = 'http://www.w3.org/2000/09/xmldsig#'
ENC_NS = 'http://www.w3.org/2001/04/xmlenc#'
WSS_BASE = 'http://docs.oasis-open.org/wss/2004/01/'
WSSE_NS = WSS_BASE + 'oasis-200401-wss-wssecurity-secext-1.0.xsd'
WSU_NS = WSS_BASE + 'oasis-200401-wss-wssecurity-utility-1.0.xsd'
BASE64B = WSS_BASE + 'oasis-200401-wss-soap-message-security-1.0#Base64Binary'
X509TOKEN = WSS_BASE + 'oasis-200401-wss-x509-token-profile-1.0#X509v3'
RSA_SHA256 = 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256'
SHA256 = 'http://www.w3.org/2001/04/xmlenc#sha256'
EET_NS = 'http://fs.mfcr.cz/eet/schema/v3'

NSMAP = {
        'soap': SOAP_NS,
        'ec': EXC_NS,
        'ds': DS_NS,
        'wsse': WSSE_NS,
        'wsu': WSU_NS,
        'eet': EET_NS,
}

DEFAULT_KEY = '''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDFCIfnLl3YjNyx
M3y2FAVovKQMetfyyj/lfLY3DoN1z/8gaVRfcqTZbwh9Btg0HafSmrWBvfgjEC/p
G9HNawYZ9nPE+WIP9bXkoOfDTmmVtX4n6OLi2Di+U7+FmPJzykV0ujsOsfcGnQ0f
63xZYoGJIwLJuz3gmAF//DfnOeTT7OUZeOKobBSYkQOKv1j05QqQZ7HP+5oq7+hN
ylFrjuEi5OAeVgJAYScE4COvcpqPKpb7OeR9f78knYFffg5zp/6bi6qkP5uGYEuu
QvbW1mATjoqbAWz8c7HNA56uNFlz8V+z9bL0f/xwQjgy4d+5qelTX46tq0vJ2XM9
dJaF8ytJAgMBAAECggEAcZ9ex9k8MyHgLqvTUiividum+q9oktFBEbTeW1eaRblB
lc5H4pb5K45VJcxpp3wmiFPBMeV8D7RI/LOXRE9ggF5YGpH5k9yNHSARJta0GqpD
6v3owQoRhuhCvOcbgdx2Oz8dyXalToIIzIx+9AjTTGMNO4onv7nIu6aWEliXdgHV
vqisMpf6GZ6O5JnwFpR4NAZSqFEDHPJUiSa6s/oyecz/4oSqcla2zla6nCHb6m83
vvb4jQ/AaoFfbCFv+oLJyZlJPGGHVyp1fvMnKV+OmLVaE7E78vXfvMvl3VHCi00p
hi3gPstjgSOqEsBWXGgoBIuvfdJkhOcBfWf5m90EgQKBgQDyaGnaCZuCSkb5axx7
rpTQjdoBaOQcnnHVF9RrOBdH3E6ZJWrxBCi3N7Aivk2AAzUBTiKb/uRtf35fbeCi
SmjXbVMjX42xFEPiJVEjqJRzmphqci/5Hq6PfB423a1TX4vECF/NRb9xbtp1IjqD
9IkwUNG/Bx/BqPWq75P7FrTrmQKBgQDQFMyaxNBx47FzZmVVc2w3mF1fxv1m3t8o
6RxT4G22eHczkZ8pOJT1UYCM8wnVEQPXmNGt85EdS7kkD4Imkyfc52MmX0pQNbDJ
XDvJYd5ZlQZ/zC9maY3ef+GZ2chs1j/0PA9Y9dvKro325RiGz+a+TWKutpRNbwqp
OvLJrFaLMQKBgAtpKNpvq1dVwcOJ7DxSOoUauFFqq5pBRyB9z60AZfAnCbghz8fq
pzQAthTcmm9VN1CJag2n0P7qintZg8J/+DFz3v8CR3w3dP6XPRuNmvdaJqSUHXf/
nr34XL++baNIEx82ObRC/UEMs9Hhu5lskGyq0UTJxA/ssSvLvU6Lgha5AoGBAKo0
CTSjvrkZ/WGepU7jTeaf2+jnFQnbTgDhxQka78MtAJwPBniqTrXnh9ZDSoydEV5+
Iy09qTqkYPmNMfGptxarsl+F3HyFnmjm6ASO6FiwXJOWikMkHiacxgWZrabRDZkS
s58Z5EICzB7jQE+tqVmKZSjyMZaxOLA6hrPOIzBRAoGAEwGiWaDbGxUoOzXsiF58
CP2VuibPIYwMwJab9bPYphW2js6MGl34S5KQLjLRQldIoW0S7m/dACF2S4ba9DSe
fvbegDaZIc/GcZQzmZdpk1RfXJPofctuHAWxPkrA3JAD8uu31FnKLuaX31+THflz
nF6OfC6QUHjZJL/WrbiUMBM=
-----END PRIVATE KEY-----'''

DEFAULT_CERT = '''-----BEGIN CERTIFICATE-----
MIID7DCCAtSgAwIBAgIEAQAABDANBgkqhkiG9w0BAQsFADBYMQswCQYDVQQGEwJD
WjEaMBgGA1UEAwwRR0ZSIEVFVCB0ZXN0IENBIDExLTArBgNVBAoMJEdlbmVyw6Fs
bsOtIGZpbmFuxI1uw60gxZllZGl0ZWxzdHbDrTAeFw0xNjA1MTkxMjQ4MjVaFw0x
ODA1MTkxMjQ4MjVaMFQxCzAJBgNVBAYTAkNaMRMwEQYDVQQDDApDWjAwMDAwMDE5
MRowGAYDVQQKDBFQcsOhdm5pY2vDoSBvc29iYTEUMBIGA1UEBRMLVDAwMDAwMDAw
MDQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDFCIfnLl3YjNyxM3y2
FAVovKQMetfyyj/lfLY3DoN1z/8gaVRfcqTZbwh9Btg0HafSmrWBvfgjEC/pG9HN
awYZ9nPE+WIP9bXkoOfDTmmVtX4n6OLi2Di+U7+FmPJzykV0ujsOsfcGnQ0f63xZ
YoGJIwLJuz3gmAF//DfnOeTT7OUZeOKobBSYkQOKv1j05QqQZ7HP+5oq7+hNylFr
juEi5OAeVgJAYScE4COvcpqPKpb7OeR9f78knYFffg5zp/6bi6qkP5uGYEuuQvbW
1mATjoqbAWz8c7HNA56uNFlz8V+z9bL0f/xwQjgy4d+5qelTX46tq0vJ2XM9dJaF
8ytJAgMBAAGjgcEwgb4wHgYDVR0RBBcwFYETZXBvZHBvcmFAZnMubWZjci5jejAf
BgNVHSMEGDAWgBR6WvwNy+w2pg3aaRlmjJvvgsOpNDAdBgNVHQ4EFgQU8oKPLNlN
Y0/h8jWEmz3EZ1O3bBMwTAYDVR0gBEUwQzBBBgpghkgBZQMCATACMDMwMQYIKwYB
BQUHAgIwJRojVGVudG8gY2VydGlmaWthdCBKRSBQT1VaRSBURVNUT1ZBQ0kwDgYD
VR0PAQH/BAQDAgbAMA0GCSqGSIb3DQEBCwUAA4IBAQBVulEYg6noEHqAW3DfNWLv
W9XdHFZQj3L5EE3Nwdd0CtMZm4/RZ/CvSENkk+GWv0YCUqHPJzhcKs0NETMKW7L6
CI+hY17rD5SHhuoCYzSMlcuMA6gZJr8wIxSWerQrvuZ4uAUMistWG9cgwETZjkGU
9JK+H98wdAm2co7WaRweDsNx04aSXagUMDAmRY/jNe7c8/HvwIdnXftbIl56wbYl
YiCIG2qS+6lVO+09EIEP40kz1PXlqFZbPLCSlT2YsYiqizfkCX/Ka+AebJykAQ3p
OqD6PQ+Y2AMAIRX8AypcN6Yj9p+oof9rda8boA8rA7wwzlJs/+ipWt2ceqPPuL9x
-----END CERTIFICATE-----'''

DEFAULT_ROOT_CERT = '''-----BEGIN CERTIFICATE-----
MIID1zCCAr+gAwIBAgIEAQAAADANBgkqhkiG9w0BAQsFADBYMQswCQYDVQQGEwJD
WjEaMBgGA1UEAwwRR0ZSIEVFVCB0ZXN0IENBIDExLTArBgNVBAoMJEdlbmVyw6Fs
bsOtIGZpbmFuxI1uw60gxZllZGl0ZWxzdHbDrTAeFw0xNjA1MDIxMTUyMjhaFw0y
NjA0MzAxMTUyMjhaMFgxCzAJBgNVBAYTAkNaMRowGAYDVQQDDBFHRlIgRUVUIHRl
c3QgQ0EgMTEtMCsGA1UECgwkR2VuZXLDoWxuw60gZmluYW7EjW7DrSDFmWVkaXRl
bHN0dsOtMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzY3JHHmqLBSI
y7EvJDYn3QfXldqf+y43RmzBKK9BE6KXGvYgmyX48CeHN00YxcjL5e6bVEXAeXYC
sbDlGNXC8YNZMhCuNF05y8yB7HyTqIVYkxjusxK3lTp+RCCIXRXhP0K8LOc6A5Pb
UbPUZhTRgeTmd4K85Nulb7A2d07zi/fHPKKHTruhLjBNY63CTaBboZ+GOlGjvHu8
9c6p8xCCiWjSNo6dagsiW1ChF4YhMI2B/h6AmOKPrbuTFivIWE5huU7KrJWE7e9L
sgRv6InahZ5+aEQ2BEvg97REsmWkh+hJhxNoge34XEdBowuGayHAmCHiHOOMDCce
PtOMtKUJuQIDAQABo4GoMIGlMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQD
AgEGMB4GA1UdEQQXMBWBE2Vwb2Rwb3JhQGZzLm1mY3IuY3owQwYDVR0gBDwwOjA4
BgpghkgBZQMCATABMCowKAYIKwYBBQUHAgIwHBoaVGF0byBDQSBqZSBwb3V6ZSBU
RVNUT1ZBQ0kwHQYDVR0OBBYEFHpa/A3L7DamDdppGWaMm++Cw6k0MA0GCSqGSIb3
DQEBCwUAA4IBAQC8f1i7D+XpcAXEnoY3UnUkFxQ4a33h8HlxFAKGUsBOHW/ZgVP8
B41BhCR+7JzbrfgWNYWUbE4TBYS/JWrNm4QwUOy2UB8nAu8Ab4bDd52eENkRiCuy
0kkT635DYtcWQebm2ajvEr0fTovBjUc9LvwOevnXfZ/eptjsh3PTjMG+w8QHQRxU
apdZtOAN/dy6x4kuqBAAFgGww9cVHpH9TYa4zukMsyepuGwEItBAjiuBDv6Lc122
QYsaCQHTMCABpVF1Ay0IuR5i7E+yPa938ZWoecFrlixYW9R+sH/Sfa8F22x4mj0c
7yVZM6k7GdvJdS9AVwAcVcGfiqzPnS1LnZYM
-----END CERTIFICATE-----'''

DEFAULT_URL = 'https://pg.eet.cz/eet/services/EETServiceSOAP/v3/'

class EETConfig(object):

    @staticmethod
    def test():
        return EETConfig('CZ00000019', 237, '/5546/RO24', debug=False, key=DEFAULT_KEY, cert=DEFAULT_CERT, root_cert=DEFAULT_ROOT_CERT)


    def __init__(self, dic, id_shop, id_register, key=None, key_file=None, key_password=None, cert=None, cert_file=None, root_cert=None, root_cert_file=None, url=None, simple=False, debug=False, dic_commission=None):
        self.debug = debug
        self.dic = dic
        self.dic_commission = dic_commission
        self.id_shop = id_shop
        self.id_register = id_register
        self.simple = simple
        self.password = None
        self.key = self._loadKey(key, key_file)
        self.cert = self._loadCert(cert, cert_file)
        self.root_crt = self._loadRootCert(cert, cert_file)
        self.url = url or DEFAULT_URL

    def _loadKey(self, key, key_file):
        if key is not None:
            return key

        elif key_file is not None and isinstance(key_file, str):
            key_file = open(key_file, 'r')

        key = key_file.read()
        key_file.close()
        return key


    def _loadCert(self, cert, cert_file):
        if cert is not None:
            return cert

        elif cert_file is not None and isinstance(cert_file, str):
            cert_file = open(cert_file, 'r')

        cert = cert_file.read()
        cert_file.close()
        return cert

    def _loadRootCert(self, cert, cert_file):
        if cert is not None:
            return cert

        elif cert_file is not None and isinstance(cert_file, str):
            cert_file = open(cert_file, 'r')

        cert = cert_file.read()
        cert_file.close()
        return cert

def ns(namespace, tagname):
    return '{%s}%s' % (namespace, tagname)
