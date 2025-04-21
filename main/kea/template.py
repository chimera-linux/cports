pkgname = "kea"
pkgver = "2.6.2"
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
sha256 = "8a50b63103734b59c3b8619ccd6766d2dfee3f02e3a5f9f3abc1cd55f70fa424"


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "kea-ctrl-agent")
    self.install_service(self.files_path / "kea-dhcp-ddns")
    self.install_service(self.files_path / "kea-dhcp4")
    self.install_service(self.files_path / "kea-dhcp6")
