pkgname = "ttyper"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Terminal based typing test"
license = "MIT"
url = "https://github.com/max-niederman/ttyper"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f7e4ff2f803483b17f35aa0c02977326a0546a95f5b465b4dd34ff17e45b4021"


def post_install(self):
    self.install_license("LICENSE.md")
