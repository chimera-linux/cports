pkgname = "xmpp-dns"
pkgver = "0.5.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "CLI tool to check XMPP SRV records"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/xmpp-dns"
source = f"{url}/-/archive/v{pkgver}/xmpp-dns-v{pkgver}.tar.gz"
sha256 = "a8bb29cde92aa80d7b4d753c225aac54a167e6324ce81717c335bdec657526e3"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/xmpp-dns.1")
