pkgname = "kdlfmt"
pkgver = "0.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Formatter for KDL documents"
license = "MIT"
url = "https://github.com/hougesen/kdlfmt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f9c2acccd781249153715f4951ba8e64abe01423c077898ff2a1ef9436df51e2"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(self.cwd / f"kdlfmt.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/kdlfmt",
                "completions",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/kdlfmt")
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"kdlfmt.{shell}", shell)
