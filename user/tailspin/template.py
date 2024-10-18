pkgname = "tailspin"
pkgver = "4.0.0"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--bins"]  # disable integration tests
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Log file highlighter"
maintainer = "sonata-chen <sonatachen39@gmail.com>"
license = "MIT"
url = "https://github.com/bensadeh/tailspin"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f13ab53eb3bd59733d3fe53a6f03dd42be3801eef7456155f520139036ffb865"


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("man/tspin.1")
    for shell in ["bash", "zsh", "fish"]:
        self.install_completion(f"completions/tspin.{shell}", shell, "tspin")
