pkgname = "nbfc-linux"
pkgver = "0.1.15"
pkgrel = 1
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
sha256 = "d1b37800886a66a6ef5a98ba45a88812fa451579028f5e4032375c62f46df535"
# no tests
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "nbfc")
    self.rm(self.destdir / "usr/lib/systemd/system/nbfc_service.service")
