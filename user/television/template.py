pkgname = "television"
pkgver = "0.11.9"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel"]
depends = ["rust-std"]
pkgdesc = "Fuzzy finder"
license = "MIT"
url = "https://github.com/alexpasmantier/television"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "be58e6011ce1228afa1c6ba15f33023484b1bc8673c466f186ac2a130bb25bdb"
# generates completions with host binary
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/tv.1")
