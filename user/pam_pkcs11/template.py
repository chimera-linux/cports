pkgname = "pam_pkcs11"
pkgver = "0.6.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-ldap",
    "--with-pcsclite",
    "--without-docbook",
]
hostmakedepends = ["automake", "gettext-devel", "pkgconf", "slibtool"]
makedepends = [
    "linux-pam-devel",
    "openldap-devel",
    "openssl3-devel",
    "pcsc-lite-devel",
]
depends = ["openssl3"]
pkgdesc = "PAM module for X.509 certificate based smart card authentication"
license = "LGPL-2.1-or-later"
url = "https://github.com/OpenSC/pam_pkcs11"
source = f"{url}/archive/refs/tags/pam_pkcs11-{pkgver}.tar.gz"
sha256 = "5d9acdb177ea2dfd7b698f6cdcc485107888cc1c9dcd15227436831c098a4075"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.rename(
        "usr/share/doc/pam_pkcs11",
        "usr/share/examples/pam_pkcs11",
        relative=False,
    )
