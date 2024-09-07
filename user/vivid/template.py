pkgname = "vivid"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Themeable LS_COLORS generator"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT AND Apache-2.0"
url = "https://github.com/sharkdp/vivid"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "88db6158dad60aba66ae16f2cd1b09f515625940a33bada65da5562a03538e49"


def post_install(self):
    self.install_license("LICENSE-MIT")
