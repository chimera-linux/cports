pkgname = "television"
pkgver = "0.13.3"
pkgrel = 0
build_style = "cargo"
make_check_env = {
    "TV_BIN_PATH": f"./target/{self.profile().triplet}/release/tv",
}
hostmakedepends = ["cargo-auditable", "pkgconf"]
depends = ["bash", "fd", "bat", "rust-std"]
checkdepends = [*depends]
pkgdesc = "Fuzzy finder"
license = "MIT"
url = "https://github.com/alexpasmantier/television"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4d3f5475fd4040ac64abc08395f4c769ffd40c9071a9a560d8038b233277b0c6"
# generates completions with host binary
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/tv.1")
