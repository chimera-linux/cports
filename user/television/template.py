pkgname = "television"
pkgver = "0.14.4"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # Passes locally, fails in CI
    "--skip=cli::special::test_tv_pipes_correctly",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
depends = ["bash", "fd", "bat", "rust-std"]
checkdepends = [*depends]
pkgdesc = "Fuzzy finder"
license = "MIT"
url = "https://github.com/alexpasmantier/television"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "039d554569117c665e1b4336c427747a118cca781ddbffaf701c4b5f01c7f3e1"
# generates completions with host binary
options = ["!cross"]

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def init_check(self):
    from cbuild.util import cargo

    self.make_check_env["TV_BIN_PATH"] = cargo.target_path(self, "tv")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/tv.1")
