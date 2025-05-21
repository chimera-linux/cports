pkgname = "zizmor"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Static analysis for GitHub Actions"
license = "MIT"
url = "https://docs.zizmor.sh"
source = (
    f"https://github.com/zizmorcore/zizmor/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6f5f4da30eb7e0fa4b7558a9418b58abd7c5ab467cb2dce330c8189a00668355"
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
