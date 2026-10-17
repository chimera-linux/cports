pkgname = "gopass-jsonapi"
pkgver = "1.17.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "JSON API for gopass"
license = "MIT"
url = "https://www.gopass.pw"
source = f"https://github.com/gopasspw/gopass-jsonapi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5cc12a3894a60fc3b0233344636638fcb04a0e834912247160e333878a60e37f"


def post_install(self):
    self.install_license("LICENSE")
