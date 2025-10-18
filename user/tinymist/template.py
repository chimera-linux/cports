pkgname = "tinymist"
pkgver = "0.13.39"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=cli", "--bin", "tinymist", "--bin", "typlite"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f33eeb8773d6cd94bc028c3a3bf87ab9a37b446562dd7ac0dd361d7e0b099dd4"
# check: takes forever
options = ["!check", "!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"tinymist.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/tinymist",
                "completion",
                shell,
                stdout=f,
            )


def install(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"tinymist.{shell}", shell)
    self.install_bin(f"target/{self.profile().triplet}/release/tinymist")
    self.install_bin(f"target/{self.profile().triplet}/release/typlite")
