pkgname = "cri-tools"
pkgver = "1.36.0"
pkgrel = 0
build_style = "makefile"
make_build_env = {"CGO_ENABLED": "1"}
make_install_env = {"BINDIR": "/usr/bin"}
hostmakedepends = ["go"]
pkgdesc = "CLI and validation tools for Kubelet Container Runtime Interface"
license = "Apache-2.0"
url = "https://github.com/kubernetes-sigs/cri-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e0433207c55e08ab9e42e2fa3b3df3769ebae7695c145b600d79878be599e08f"
# check: no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
