pkgname = "zola"
pkgver = "0.19.2"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "oniguruma-devel"]
pkgdesc = "Static site generator"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.getzola.org"
source = f"https://github.com/getzola/zola/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bae10101b4afff203f781702deeb0a60d3ab0c9f0c7a616a7c1e0c504c33c93f"
# generates completions with host bins
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "runs out of memory during linking"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"zola.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/zola",
                "completion",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/zola")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"zola.{shell}", shell)
    self.install_license("LICENSE")
