pkgname = "go-sendxmpp"
pkgver = "0.15.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Tool to send messages or files over XMPP"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/go-sendxmpp"
source = f"{url}/-/archive/v{pkgver}/go-sendxmpp-v{pkgver}.tar.gz"
sha256 = "35efac1a27740888dbb047056bb1a159659e910f11e2637e06c1768e5047c222"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE-mellium")
    self.install_man("man/go-sendxmpp.1")
    self.install_man("man/go-sendxmpp.5")
