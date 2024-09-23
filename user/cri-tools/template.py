pkgname = "cri-tools"
pkgver = "1.31.1"
pkgrel = 0
build_style = "makefile"
make_build_env = {"CGO_ENABLED": "1"}
make_install_env = {"BINDIR": "/usr/bin"}
hostmakedepends = ["go"]
pkgdesc = "CLI and validation tools for Kubelet Container Runtime Interface"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "Apache-2.0"
url = "https://github.com/kubernetes-sigs/cri-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "465bd14768a86a782c6e4b15b3683c4a5efd0363d68b241d5757a7bada9bcd21"
# check: no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
