pkgname = "sad"
pkgver = "0.4.31"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "python"]
makedepends = ["rust-std"]
pkgdesc = "CLI search and replace"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/ms-jpq/sad"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c717e54798e21356340271e32e43de5b05ba064ae64edf639fede27b1ed15ceb"


def post_install(self):
    self.install_license("LICENSE")
