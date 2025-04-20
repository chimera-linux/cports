pkgname = "k9s"
pkgver = "0.50.4"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags= -X github.com/derailed/k9s/cmd.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal UI to interact with Kubernetes clusters"
license = "Apache-2.0"
url = "https://k9scli.io"
source = f"https://github.com/derailed/k9s/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4f7f6702145b0eea2f42c684ff823aa261bc80b1a3b2a33b56fb6f87d7755c73"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"k9s.{shell}", "w") as outf:
            self.do("build/k9s", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"k9s.{shell}", shell)
