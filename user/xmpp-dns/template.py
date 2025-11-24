pkgname = "xmpp-dns"
pkgver = "0.5.4"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "CLI tool to check XMPP SRV records"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/xmpp-dns"
source = f"{url}/-/archive/v{pkgver}/xmpp-dns-v{pkgver}.tar.gz"
sha256 = "1b23824a443ffa84ab3cfece67c90116d7b9ba66e2ea9410d40ca1eb4ea2f72f"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/xmpp-dns.1")
