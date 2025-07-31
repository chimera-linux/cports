pkgname = "zizmor"
pkgver = "1.11.0"
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
sha256 = "e60c8c280bee3b3a7eba32a961f6aa23d229f7a9db754715b7c98362a7c6dc7f"
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
