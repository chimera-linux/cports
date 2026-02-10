pkgname = "age"
pkgver = "1.3.1"
pkgrel = 1
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
sha256 = "396007bc0bc53de253391493bda1252757ba63af1a19db86cfb60a35cb9d290a"


def post_install(self):
    self.install_man("doc/*.1", glob=True)
    self.install_license("LICENSE")
