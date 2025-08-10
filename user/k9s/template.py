pkgname = "k9s"
pkgver = "0.50.9"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags= -X github.com/derailed/k9s/cmd.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal UI to interact with Kubernetes clusters"
license = "Apache-2.0"
url = "https://k9scli.io"
source = f"https://github.com/derailed/k9s/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7496cfc6da6da5d91ef2ad5ea61eae15186effabb77adf904c896213ca6ff810"
# cross: generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"k9s.{shell}", "w") as outf:
            self.do("build/k9s", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"k9s.{shell}", shell)
