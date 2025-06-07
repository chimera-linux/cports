pkgname = "tailspin"
pkgver = "5.4.4"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--bins"]  # disable integration tests
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Log file highlighter"
license = "MIT"
url = "https://github.com/bensadeh/tailspin"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5c7829245c1b02cc19e0c5a23222ab955dd0b36e8c11e135db4257e393a7c236"


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("man/tspin.1")
    for shell in ["bash", "zsh", "fish"]:
        self.install_completion(f"completions/tspin.{shell}", shell, "tspin")
