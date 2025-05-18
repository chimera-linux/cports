pkgname = "nbfc-linux"
pkgver = "0.3.16"
pkgrel = 0
build_style = "makefile"
make_build_args = ["confdir=/etc"]
make_install_args = ["confdir=/etc"]
makedepends = ["curl-devel", "linux-headers", "openssl3-devel"]
pkgdesc = "NoteBook FanControl for Linux"
license = "GPL-3.0-or-later"
url = "https://github.com/nbfc-linux/nbfc-linux"
source = f"{url}/archive/{pkgver}/nbfc-linux-{pkgver}.tar.gz"
sha256 = "3661c6335a6ef357e69d03bfa7e1ca3b19d2465ef4a942332514e3dd818fda7a"
# recursive json parser
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# no tests
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "argparser compiletime constant stuff"


def post_install(self):
    self.install_service(self.files_path / "nbfc")
    self.uninstall("usr/lib/systemd")
