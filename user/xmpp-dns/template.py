pkgname = "xmpp-dns"
pkgver = "0.5.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "CLI tool to check XMPP SRV records"
license = "BSD-2-Clause"
url = "https://salsa.debian.org/mdosch/xmpp-dns"
source = f"{url}/-/archive/v{pkgver}/xmpp-dns-v{pkgver}.tar.gz"
sha256 = "f071924999071cabe49edfc9b33a54a1cfcc12c0e14d3ebc0a5a1c06a33d6049"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/xmpp-dns.1")
