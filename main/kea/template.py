pkgname = "kea"
pkgver = "3.0.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Drunstatedir=run"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "dinit-chimera",
    "gtest-devel",
    "log4cplus",
    "openssl3-devel",
    "python-devel",
]
checkdepends = ["procps"]
pkgdesc = "Alternative DHCP implementation by ISC"
license = "MPL-2.0"
url = "https://kea.isc.org"
source = f"https://downloads.isc.org/isc/kea/cur/{pkgver[: pkgver.rfind('.')]}/kea-{pkgver}.tar.xz"
sha256 = "ec84fec4bb7f6b9d15a82e755a571e9348eb4d6fbc62bb3f6f1296cd7a24c566"


def post_install(self):
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/kea-ctrl-agent")
    self.install_service("^/kea-dhcp-ddns")
    self.install_service("^/kea-dhcp4")
    self.install_service("^/kea-dhcp6")


@subpackage("kea-devel")
def _(self):
    return self.default_devel()
