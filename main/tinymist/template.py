pkgname = "tinymist"
pkgver = "0.11.32"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "tinymist"]
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "877d0c3722ac863d5f6f6469bd8b7b9a7ee461a2e4f50310ed0d42b795c1f182"
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
