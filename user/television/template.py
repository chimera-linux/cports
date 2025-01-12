pkgname = "television"
pkgver = "0.9.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel"]
depends = ["rust-std"]
pkgdesc = "Fuzzy finder"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/alexpasmantier/television"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "93f82f33e699a4a91f0015d88856a7fde5ae95bfa132a02c08518ddd264256cb"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
