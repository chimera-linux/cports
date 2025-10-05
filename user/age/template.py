pkgname = "age"
pkgver = "1.2.1"
pkgrel = 9
build_style = "go"
make_build_args = [f"-ldflags=-X main.Version={pkgver}", "./cmd/..."]
hostmakedepends = ["go"]
pkgdesc = "File encryption tool"
license = "BSD-3-Clause"
url = "https://github.com/FiloSottile/age"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "93bd89a16c74949ee7c69ef580d8e4cf5ce03e7d9c461b68cf1ace3e4017eef5"


def post_install(self):
    self.install_man("doc/*.1", glob=True)
    self.install_license("LICENSE")
