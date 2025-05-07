pkgname = "nbfc-linux"
pkgver = "0.3.14"
pkgrel = 0
build_style = "makefile"
make_build_args = ["confdir=/etc"]
make_install_args = ["confdir=/etc"]
makedepends = ["curl-devel", "linux-headers", "openssl-devel"]
pkgdesc = "NoteBook FanControl for Linux"
license = "GPL-3.0-or-later"
url = "https://github.com/nbfc-linux/nbfc-linux"
source = f"{url}/archive/{pkgver}/nbfc-linux-{pkgver}.tar.gz"
sha256 = "f49eba952c31396f858a6b338d68ea8c66b2ebc0659a49296f2d851f284a9969"
# recursive json parser
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# no tests
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "argparser compiletime constant stuff"


def post_install(self):
    self.install_service(self.files_path / "nbfc")
    self.uninstall("usr/lib/systemd")
