pkgname = "glow"
pkgver = "2.1.0"
pkgrel = 4
build_style = "go"
# needs net
make_check_args = ["-skip", "TestGlowSources", "./..."]
hostmakedepends = ["go"]
pkgdesc = "Render markdown on the CLI"
license = "MIT"
url = "https://github.com/charmbracelet/glow"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f1875a73ed81e5d8e6c81443e9a9d18bd9d1489c563c9fa2ff5425f2f8e2af6f"
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
