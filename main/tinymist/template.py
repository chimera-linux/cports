pkgname = "tinymist"
pkgver = "0.12.14"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=cli", "--bin", "tinymist", "--bin", "typlite"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "24bd7b64487158f41ca980066fff3b9b95b2d5367d364c62b23974f6a82cfd32"
# takes forever
options = ["!check"]

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
