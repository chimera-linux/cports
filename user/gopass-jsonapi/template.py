pkgname = "gopass-jsonapi"
pkgver = "1.17.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "JSON API for gopass"
license = "MIT"
url = "https://www.gopass.pw"
source = f"https://github.com/gopasspw/gopass-jsonapi/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b1369a2bad432386455d7aa3002f93910f9e275fc3c33e3f37f5731aa918f07a"


def post_install(self):
    self.install_license("LICENSE")
