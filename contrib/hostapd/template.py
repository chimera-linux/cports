pkgname = "hostapd"
pkgver = "2.10"
pkgrel = 0
build_wrksrc = "hostapd"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["BINDIR=/usr/bin"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["gmake", "libnl-devel", "linux-headers", "openssl-devel"]
pkgdesc = "IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://w1.fi/hostapd"
source = f"https://w1.fi/releases/hostapd-{pkgver}.tar.gz"
sha256 = "206e7c799b678572c2e3d12030238784bc4a9f82323b0156b4c9466f1498915d"
# No tests available
options = ["!check"]


def init_configure(self):
    self.cp("defconfig", ".config")


def post_install(self):
    self.install_license("README")
    self.install_service(self.files_path / "hostapd")
