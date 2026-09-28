pkgname = "gopass-jsonapi"
pkgver = "1.17.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "JSON API for gopass"
license = "MIT"
url = "https://www.gopass.pw"
source = f"https://github.com/gopasspw/gopass-jsonapi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4b2c0fc019b2667af845202059103f70d684d924a5dc0590469f825ca7d251d3"


def post_install(self):
    self.install_license("LICENSE")
