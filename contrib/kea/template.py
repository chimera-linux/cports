pkgname = "kea"
pkgver = "2.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-shell",
]
hostmakedepends = [
    "automake",
    "libtool",
]
makedepends = [
    "boost-devel",
    "gtest-devel",
    "log4cplus",
    "openssl-devel",
    "python-devel",
]
checkdepends = ["procps"]
pkgdesc = "Alternative DHCP implementation by ISC"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "MPL-2.0"
url = "https://kea.isc.org"
source = f"https://downloads.isc.org/isc/kea/cur/{pkgver[:pkgver.rfind('.')]}/kea-{pkgver}.tar.gz"
sha256 = "207ceae33eb3b81ec4e6ac5605249a85b93779333b62aadf39e489f11dbcdc8d"


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "kea-ctrl-agent")
    self.install_service(self.files_path / "kea-dhcp-ddns")
    self.install_service(self.files_path / "kea-dhcp4")
    self.install_service(self.files_path / "kea-dhcp6")
