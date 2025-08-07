pkgname = "xmpp-dns"
pkgver = "0.4.5"
pkgrel = 5
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "CLI tool to check XMPP SRV records"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/xmpp-dns"
source = f"{url}/-/archive/v{pkgver}/xmpp-dns-v{pkgver}.tar.gz"
sha256 = "ce4ee08577f9a84828d234790af85e4031727eaf37900f0fccc4ceeb92616239"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/xmpp-dns.1")
