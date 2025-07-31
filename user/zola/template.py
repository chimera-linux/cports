pkgname = "zola"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "oniguruma-devel"]
pkgdesc = "Static site generator"
license = "MIT"
url = "https://www.getzola.org"
source = f"https://github.com/getzola/zola/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bbfbc0496cf6612b6030c6d97b0fd2567f5ec41e251f8874b6c9ccda4c8149d4"
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
