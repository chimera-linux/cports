pkgname = "kea"
pkgver = "3.0.2"
pkgrel = 0
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
sha256 = "29f4e44fa48f62fe15158d17411e003496203250db7b3459c2c79c09f379a541"


def post_install(self):
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/kea-ctrl-agent")
    self.install_service("^/kea-dhcp-ddns")
    self.install_service("^/kea-dhcp4")
    self.install_service("^/kea-dhcp6")


@subpackage("kea-devel")
def _(self):
    return self.default_devel()
