pkgname = "rbw"
pkgver = "1.12.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Unofficial Bitwarden CLI"
maintainer = "sewn <sewn@disroot.org>"
license = "MIT"
url = "https://github.com/doy/rbw"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c564484f1054a85014b6b2a1fbade24d56b1b221dbac681c682ffaeba158b697"


def post_install(self):
    self.install_license("LICENSE")
