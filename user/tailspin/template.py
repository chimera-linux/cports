pkgname = "tailspin"
pkgver = "5.4.5"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--bins"]  # disable integration tests
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Log file highlighter"
license = "MIT"
url = "https://github.com/bensadeh/tailspin"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8dec5333c8f3e9cb6f29b4823482634b3c10e317aae12d0844d73ccfb1307a13"


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("man/tspin.1")
    for shell in ["bash", "zsh", "fish"]:
        self.install_completion(f"completions/tspin.{shell}", shell, "tspin")
