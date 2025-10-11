pkgname = "kdlfmt"
pkgver = "0.1.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Formatter for KDL documents"
license = "MIT"
url = "https://github.com/hougesen/kdlfmt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "56dfb8f20050fddfbf2b0c1afb42911de97c97687c4d6c118dad643caf82cabd"
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
