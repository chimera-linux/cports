pkgname = "nbfc-linux"
pkgver = "0.3.18"
pkgrel = 0
build_style = "makefile"
make_build_args = ["confdir=/etc"]
make_install_args = ["confdir=/etc"]
makedepends = ["curl-devel", "dinit-chimera", "linux-headers", "openssl3-devel"]
pkgdesc = "NoteBook FanControl for Linux"
license = "GPL-3.0-or-later"
url = "https://github.com/nbfc-linux/nbfc-linux"
source = f"{url}/archive/{pkgver}/nbfc-linux-{pkgver}.tar.gz"
sha256 = "5700c1574dd34ecfe02bcfd09bc0deadcc50365d054f5607e849ddaa80ef8f0b"
# recursive json parser
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# no tests
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "argparser compiletime constant stuff"


def post_install(self):
    self.install_service("^/nbfc")
    self.uninstall("usr/lib/systemd")
