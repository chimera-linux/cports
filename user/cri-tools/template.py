pkgname = "cri-tools"
pkgver = "1.35.0"
pkgrel = 0
build_style = "makefile"
make_build_env = {"CGO_ENABLED": "1"}
make_install_env = {"BINDIR": "/usr/bin"}
hostmakedepends = ["go"]
pkgdesc = "CLI and validation tools for Kubelet Container Runtime Interface"
license = "Apache-2.0"
url = "https://github.com/kubernetes-sigs/cri-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0edaa2bd4a6d44fc0406e1b4f45421e17b2ff7d49b2d76e57aba15eef25580bd"
# check: no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
