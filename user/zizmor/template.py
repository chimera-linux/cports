pkgname = "zizmor"
pkgver = "1.14.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Static analysis for GitHub Actions"
license = "MIT"
url = "https://docs.zizmor.sh"
source = (
    f"https://github.com/zizmorcore/zizmor/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c2b0d5edcb3a008b62412522740885bd75164cb4239bb2acd4007acaad60815a"
# Generates completions using host binaries
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"zizmor.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/zizmor",
                "--completions",
                shell,
                stdout=f,
            )


def install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/zizmor")
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"zizmor.{shell}", shell)
    self.install_license("LICENSE")
