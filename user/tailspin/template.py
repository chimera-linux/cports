pkgname = "tailspin"
pkgver = "3.0.2"
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
sha256 = "6a54127187fc894ca5c58d0f65108769c9c2ac022185f29b87818aaa4150ed0b"


def post_install(self):
    self.install_license("LICENCE")
    self.install_man("man/tspin.1")
    for shell in ["bash", "zsh", "fish"]:
        self.install_completion(f"completions/tspin.{shell}", shell)
