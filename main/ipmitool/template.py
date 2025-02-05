pkgname = "ipmitool"
pkgver = "1.8.19"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-intf-free",
    "--enable-intf-imb",
    "--enable-intf-lanplus",
    "--enable-intf-open",
    "--enable-intf-usb",
    "--enable-ipmishell",
]
make_dir = "."
hostmakedepends = ["automake", "libtool"]
makedepends = [
    "linux-headers",
    "openssl3-devel",
    "readline-devel",
]
pkgdesc = "CLI to manage IPMI systems"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://codeberg.org/IPMITool/ipmitool"
source = f"{url}/archive/IPMITOOL_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "ce13c710fea3c728ba03a2a65f2dd45b7b13382b6f57e25594739f2e4f20d010"


def post_install(self):
    self.install_license("COPYING")
