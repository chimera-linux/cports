pkgname = "go-sendxmpp"
pkgver = "0.15.5"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Tool to send messages or files over XMPP"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/go-sendxmpp"
source = f"{url}/-/archive/v{pkgver}/go-sendxmpp-v{pkgver}.tar.gz"
sha256 = "57c24a82689461f7af4c8c9233f548ecc4d1deedad6d9f9e43d1b4c6af8238d6"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE-mellium")
    self.install_man("man/go-sendxmpp.1")
    self.install_man("man/go-sendxmpp.5")
