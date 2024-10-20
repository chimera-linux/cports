pkgname = "tinymist"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "tinymist"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4b919f2a823b727edb6601d9675a2716baa816ea5e510b09fea4d0d696cc31a0"
# takes forever
options = ["!check"]


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
