pkgname = "television"
pkgver = "0.11.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel"]
depends = ["rust-std"]
pkgdesc = "Fuzzy finder"
license = "MIT"
url = "https://github.com/alexpasmantier/television"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c4e8a87d65135fb5a6006c7c08dd34cf6aeb24c2d59e9ea6772e9ff714bfed29"
# generates completions with host binary
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/tv.1")
