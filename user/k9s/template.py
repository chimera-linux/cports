pkgname = "k9s"
pkgver = "0.50.5"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags= -X github.com/derailed/k9s/cmd.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Terminal UI to interact with Kubernetes clusters"
license = "Apache-2.0"
url = "https://k9scli.io"
source = f"https://github.com/derailed/k9s/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "86dd0d54f3bcd1ea57d383982d85c3e31fe7af5dcdb87cc0dc19ec6bf815170a"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"k9s.{shell}", "w") as outf:
            self.do("build/k9s", "completion", shell, stdout=outf)


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"k9s.{shell}", shell)
