pkgname = "go-sendxmpp"
pkgver = "0.14.1"
pkgrel = 5
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Tool to send messages or files over XMPP"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/go-sendxmpp"
source = f"{url}/-/archive/v{pkgver}/go-sendxmpp-v{pkgver}.tar.gz"
sha256 = "3221a8a563153d1dfab367e7588e0e1991ceb6b3cf41e2e525351d476f12d887"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE-mellium")
    self.install_man("man/go-sendxmpp.1")
    self.install_man("man/go-sendxmpp.5")
