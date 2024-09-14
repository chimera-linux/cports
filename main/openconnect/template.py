pkgname = "openconnect"
pkgver = "9.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-vpnc-script=/usr/libexec/vpnc-script"]
hostmakedepends = [
    "automake",
    "gettext",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gnutls-devel",
    "heimdal-devel",
    "libproxy-devel",
    "libtasn1-devel",
    "libxml2-devel",
    "linux-headers",
    "lz4-devel",
    "p11-kit-devel",
    "pcsc-lite-devel",
    "tpm2-tss-devel",
    "trousers-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["bash"]
depends = ["vpnc-scripts"]
pkgdesc = "Multi-protocol SSL VPN client"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-only"
url = "https://www.infradead.org/openconnect"
source = f"{url}/download/openconnect-{pkgver}.tar.gz"
sha256 = "a2bedce3aa4dfe75e36e407e48e8e8bc91d46def5335ac9564fbf91bd4b2413e"


@subpackage("openconnect-devel")
def _(self):
    return self.default_devel()
