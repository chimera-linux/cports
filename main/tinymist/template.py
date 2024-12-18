pkgname = "tinymist"
pkgver = "0.12.10"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "tinymist", "--bin", "typlite"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["rust-std", "openssl-devel"]
depends = ["typst"]
pkgdesc = "Language server for Typst"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://myriad-dreamin.github.io/tinymist"
source = f"https://github.com/Myriad-Dreamin/tinymist/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "65d12ed3c385d10d8ffda7f1234020b2fa21ee29f323d8e0f4bbfbe46a59d62b"
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
    self.install_bin(f"target/{self.profile().triplet}/release/typlite")
