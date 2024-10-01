pkgname = "glow"
pkgver = "2.0.0"
pkgrel = 1
build_style = "go"
# needs net
make_check_args = ["-skip", "TestGlowSources", "./..."]
hostmakedepends = ["go"]
pkgdesc = "Render markdown on the CLI"
maintainer = "xunil-cloud <river_electron@proton.me>"
license = "MIT"
url = "https://github.com/charmbracelet/glow"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "55872e36c006e7e715b86283baf14add1f85b0a0304e867dd0d80e8d7afe49a8"
# uses binary for completions
options = ["!cross"]


def post_build(self):
    with open(self.cwd / "glow.1", "w") as f:
        self.do(f"{self.make_dir}/glow", "man", stdout=f)
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"glow.{shell}", "w") as f:
            self.do(f"{self.make_dir}/glow", "completion", shell, stdout=f)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"glow.{shell}", shell)
    self.install_man("glow.1")
    self.install_license("LICENSE")
