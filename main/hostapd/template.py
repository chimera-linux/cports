pkgname = "hostapd"
pkgver = "2.11"
pkgrel = 0
build_wrksrc = "hostapd"
build_style = "makefile"
make_install_args = ["BINDIR=/usr/bin"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["libnl-devel", "linux-headers", "openssl3-devel"]
pkgdesc = "IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://w1.fi/hostapd"
source = f"https://w1.fi/releases/hostapd-{pkgver}.tar.gz"
sha256 = "2b3facb632fd4f65e32f4bf82a76b4b72c501f995a4f62e330219fe7aed1747a"
# No tests available
options = ["!check"]


def init_configure(self):
    self.cp("defconfig", ".config")


def post_install(self):
    self.install_license("README")
    self.install_service(self.files_path / "hostapd")
