pkgname = "kea"
pkgver = "2.6.3"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-shell",
]
hostmakedepends = [
    "automake",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "gtest-devel",
    "log4cplus",
    "openssl3-devel",
    "python-devel",
]
checkdepends = ["procps"]
pkgdesc = "Alternative DHCP implementation by ISC"
license = "MPL-2.0"
url = "https://kea.isc.org"
source = f"https://downloads.isc.org/isc/kea/cur/{pkgver[: pkgver.rfind('.')]}/kea-{pkgver}.tar.gz"
sha256 = "00241a5955ffd3d215a2c098c4527f9d7f4b203188b276f9a36250dd3d9dd612"


def post_install(self):
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_service("^/kea-ctrl-agent")
    self.install_service("^/kea-dhcp-ddns")
    self.install_service("^/kea-dhcp4")
    self.install_service("^/kea-dhcp6")
