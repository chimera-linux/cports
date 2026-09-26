pkgname = "age"
pkgver = "1.3.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.Version={pkgver}",
    "./cmd/...",
    "./extra/...",
]
hostmakedepends = ["go"]
pkgdesc = "File encryption tool"
license = "BSD-3-Clause"
url = "https://github.com/FiloSottile/age"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b07c28c6c4bdafa272073a310b75bc22c49da8904585a89c30e5ca4233e63843"


def post_install(self):
    self.install_man("doc/*.1", glob=True)
    self.install_license("LICENSE")
