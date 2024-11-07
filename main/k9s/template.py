pkgname = "k9s"
pkgver = "0.32.5"
pkgrel = 5
build_style = "go"
make_build_args = [f"-ldflags= -X github.com/derailed/k9s/cmd.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal UI to interact with Kubernetes clusters"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://k9scli.io"
source = f"https://github.com/derailed/k9s/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e011697b3de99d7691119036eaae6e5d4f1a98e284755ab6b15ae6daba08595f"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"k9s.{shell}", "w") as outf:
            self.do("build/k9s", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"k9s.{shell}", shell)
