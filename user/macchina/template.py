pkgname = "macchina"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "System information frontend"
license = "MIT"
url = "https://github.com/Macchina-CLI/macchina"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "edd7591565f199c1365420655a144507bcd2838aed09b79fefdc8b661180432f"


def post_install(self):
    self.install_license("LICENSE")
