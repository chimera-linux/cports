pkgname = "tailspin"
pkgver = "5.5.0"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--bins"]  # disable integration tests
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Log file highlighter"
license = "MIT"
url = "https://github.com/bensadeh/tailspin"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e9d7cefb865585bb048a2ccbfcc1f900ae344134d71132a7c48ee0d5af09cdaf"

if self.profile().arch == "loongarch64":
    broken = "busted rustix"


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("man/tspin.1")
    for shell in ["bash", "zsh", "fish"]:
        self.install_completion(f"completions/tspin.{shell}", shell, "tspin")
