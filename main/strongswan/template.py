pkgname = "strongswan"
pkgver = "6.0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",
    "--with-ipsecdir=/usr/lib/strongswan",
    "--with-capabilities=libcap",
    "--with-user=_strongswan",
    "--with-group=_strongswan",
    "--disable-aes",
    "--disable-des",
    "--disable-eap-gtc",
    "--disable-hmac",
    "--disable-md5",
    "--disable-mysql",
    "--disable-rc2",
    "--disable-sha1",
    "--disable-sha2",
    "--disable-static",
    "--enable-addrblock",
    "--enable-attr-sql",
    "--enable-blowfish",
    "--enable-bypass-lan",
    "--enable-cmd",
    "--enable-conftest",
    "--enable-curl",
    "--enable-eap-aka",
    "--enable-eap-aka-3gpp2",
    "--enable-eap-dynamic",
    "--enable-eap-identity",
    "--enable-eap-md5",
    "--enable-eap-mschapv2",
    "--enable-eap-peap",
    "--enable-eap-radius",
    "--enable-eap-sim",
    "--enable-eap-sim-file",
    "--enable-eap-simaka-pseudonym",
    "--enable-eap-simaka-reauth",
    "--enable-eap-tls",
    "--enable-eap-ttls",
    "--enable-gcm",
    "--enable-gmp",
    "--enable-ha",
    "--enable-ikev1",
    "--enable-ipseckey",
    "--enable-ldap",
    "--enable-md4",
    "--enable-openssl",
    "--enable-pkcs11",
    "--enable-pki",
    "--enable-python-eggs",
    "--enable-shared",
    "--enable-sqlite",
    "--enable-stroke",
    "--enable-swanctl",
    "--enable-unbound",
    "--enable-unity",
    "--enable-vici",
    "--enable-whitelist",
    "--enable-xauth-eap",
    "--enable-xauth-generic",
    "--enable-xauth-pam",
]
hostmakedepends = ["automake", "slibtool", "pkgconf"]
makedepends = [
    "gettext-devel",
    "gmp-devel",
    "libcap-devel",
    "curl-devel",
    "ldns-devel",
    "linux-headers",
    "linux-pam-devel",
    "openldap-devel",
    "openssl3-devel",
    "sqlite-devel",
    "unbound-devel",
]
pkgdesc = "Open Source IKEv2 IPsec-based VPN solution"
license = "GPL-2.0-or-later"
url = "https://www.strongswan.org"
source = f"https://download.strongswan.org/strongswan-{pkgver}.tar.bz2"
sha256 = "212368cbc674fed31f3292210303fff06da8b90acad2d1387375ed855e6879c4"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/strongswan")
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
