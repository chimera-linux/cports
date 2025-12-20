pkgname = "mdbook"
pkgver = "0.5.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Utility to create online books from markdown files"
license = "MPL-2.0"
url = "https://rust-lang.github.io/mdBook"
source = (
    f"https://github.com/rust-lang/mdBook/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "2c8615a17c5670f9aa6d8dbf77c343cf430f95f571f28a87bb7aaa8f29c1ac5b"
# Generates completions using host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"mdbook.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/mdbook",
                "completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"mdbook.{shell}", shell)
