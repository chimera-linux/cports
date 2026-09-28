pkgname = "flash-watcher"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "File watcher that executes commands when files change"
license = "MIT"
url = "https://github.com/sage-scm/Flash"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3ee5e18457f29919c01aad879ce964348f5ee0b549800dedf8eb20009313a235"


def post_install(self):
    self.install_license("LICENSE")
