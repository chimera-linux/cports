pkgname = "kea"
pkgver = "2.6.1"
pkgrel = 2
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
    "openssl-devel",
    "python-devel",
]
checkdepends = ["procps"]
pkgdesc = "Alternative DHCP implementation by ISC"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "MPL-2.0"
url = "https://kea.isc.org"
source = f"https://downloads.isc.org/isc/kea/cur/{pkgver[: pkgver.rfind('.')]}/kea-{pkgver}.tar.gz"
sha256 = "d2ce14a91c2e248ad2876e29152d647bcc5e433bc68dafad0ee96ec166fcfad1"


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "kea-ctrl-agent")
    self.install_service(self.files_path / "kea-dhcp-ddns")
    self.install_service(self.files_path / "kea-dhcp4")
    self.install_service(self.files_path / "kea-dhcp6")
