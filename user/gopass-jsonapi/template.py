pkgname = "gopass-jsonapi"
pkgver = "1.16.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Gopass Browser Bindings"
license = "MIT"
url = "https://www.gopass.pw"
source = f"https://github.com/gopasspw/gopass-jsonapi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "73449a7c359836a995946e54d91e32afe5a54e1519b5a01f78c9923c13c0894f"


def post_install(self):
    self.install_license("LICENSE")
