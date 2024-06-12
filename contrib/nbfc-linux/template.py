pkgname = "nbfc-linux"
pkgver = "0.2.7"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["confdir=/etc"]
make_install_args = ["confdir=/etc"]
hostmakedepends = ["gmake"]
pkgdesc = "NoteBook FanControl for Linux"
maintainer = "Sid Pranjale <mail@sidonthe.net>"
license = "GPL-3.0-or-later"
url = "https://github.com/nbfc-linux/nbfc-linux"
source = f"{url}/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5915af1fd3c23bdb8289cc9428fad825daf49dc187b50bbe759c317c9785bd35"
# no tests
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "nbfc")
