pkgname = "television"
pkgver = "0.13.11"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # Passes locally, fails in CI
    "--skip=cli::special::test_tv_pipes_correctly",
]
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
sha256 = "a524e0cb07224794df7fda729a0aa90d77d7dfbb87a1a46a9b3b1a3c838532d5"
# generates completions with host binary
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/tv.1")
