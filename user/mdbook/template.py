pkgname = "mdbook"
pkgver = "0.5.1"
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
sha256 = "41a20de21e6a57942ec4e41b049babe8dac77b246a0549b87631cee0d2e75b2c"
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
