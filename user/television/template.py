pkgname = "television"
pkgver = "0.10.0"
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
sha256 = "62dbc15b4109be90ef7bda6993523223aa6f89f39333ea8d35d515edc4ccb98d"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
