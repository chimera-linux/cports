pkgname = "lidm"
pkgver = "2.0.2"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "dinit-chimera",
    "linux-headers",
    "linux-pam-devel",
]
pkgdesc = "Customizable TUI display manager"
license = "GPL-3.0-only"
url = "https://github.com/javalsai/lidm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "08bb013df15987b5a685c5925a41b2c9a8531e4af3c9a097c0dbb1fa8a6d8a79"
# no test suite, files in /etc
options = ["!check", "etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "lidm")
