pkgname = "glow"
pkgver = "2.1.1"
pkgrel = 0
build_style = "go"
# needs net
make_check_args = ["-skip", "TestGlowSources", "./..."]
hostmakedepends = ["go"]
pkgdesc = "Render markdown on the CLI"
license = "MIT"
url = "https://github.com/charmbracelet/glow"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f13e1d6be1ab4baf725a7fedc4cd240fc7e5c7276af2d92f199e590e1ef33967"
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
