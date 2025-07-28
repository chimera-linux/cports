pkgname = "direnv"
pkgver = "2.37.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Environment variables loader"
license = "MIT"
url = "https://github.com/direnv/direnv"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4142fbb661f3218913fac08d327c415e87b3e66bd0953185294ff8f3228ead24"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/*.1", glob=True)
