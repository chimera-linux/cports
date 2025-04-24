pkgname = "direnv"
pkgver = "2.36.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Environment variables loader"
license = "MIT"
url = "https://github.com/direnv/direnv"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "edb89ca67ef46a792d4e20177dae9dbd229e26dcbcfb17baa9645c1ff7cc47b0"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/*.1", glob=True)
