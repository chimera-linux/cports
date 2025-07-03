pkgname = "direnv"
pkgver = "2.37.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Environment variables loader"
license = "MIT"
url = "https://github.com/direnv/direnv"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6302f3eb824ae5f7d33475c6e9ac0ec46a228e282fca7dba881f3536575a25c8"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/*.1", glob=True)
