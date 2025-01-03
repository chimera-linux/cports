pkgname = "nbfc-linux"
pkgver = "0.2.7"
pkgrel = 2
build_style = "makefile"
make_build_args = ["confdir=/etc"]
make_install_args = ["confdir=/etc"]
pkgdesc = "NoteBook FanControl for Linux"
maintainer = "Sid Pranjale <mail@sidonthe.net>"
license = "GPL-3.0-or-later"
url = "https://github.com/nbfc-linux/nbfc-linux"
source = f"{url}/archive/{pkgver}/nbfc-linux-{pkgver}.tar.gz"
sha256 = "5915af1fd3c23bdb8289cc9428fad825daf49dc187b50bbe759c317c9785bd35"
# recursive json parser
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# no tests
options = ["!check"]

if self.profile().arch == "ppc":
    broken = "argparser compiletime constant stuff"


def post_install(self):
    self.install_service(self.files_path / "nbfc")
