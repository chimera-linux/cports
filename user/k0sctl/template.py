pkgname = "k0sctl"
pkgver = "0.23.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Bootstrapping and management tool for k0s clusters"
license = "Apache-2.0"
url = "https://github.com/k0sproject/k0sctl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6b3e93c2bd27b0a881160c3128061e31498ab1e4086adf7f419b1d06fdbe9ecb"
# generates completions by running the target binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"k0sctl.{shell}", "w") as f:
            self.do(
                f"{self.make_dir}/k0sctl",
                "completion",
                "--shell",
                shell,
                stdout=f,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"k0sctl.{shell}", shell)
