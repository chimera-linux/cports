pkgname = "zizmor"
pkgver = "1.15.2"
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
sha256 = "a3d3a062ffd79f3958c7d428a9aeb8b6332d57bc3fb15bed242d519aa11e2f42"
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
