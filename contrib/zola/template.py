pkgname = "zola"
pkgver = "0.18.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl-devel", "oniguruma-devel"]
pkgdesc = "Static site generator"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/getzola/zola"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c0e1711a68bc005c2e0ecc76a468f3459739c9e54af34850cb725d04391e19b5"
# generates completions with host bins
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"zola.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/zola",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"zola.{shell}", shell)
    self.install_license("LICENSE")
