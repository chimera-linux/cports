pkgname = "obfs4proxy"
pkgver = "0.0.14"
pkgrel = 0
build_style = "go"
make_build_args = ["./obfs4proxy"]
hostmakedepends = ["go"]
pkgdesc = "Circumvents censorship by transforming client-to-bridge Tor traffic"
license = "GPL-3.0-or-later"
url = "https://github.com/Yawning/obfs4"
source = f"{url}/archive/refs/tags/obfs4proxy-{pkgver}.tar.gz"
sha256 = "a4b7520e732b0f168832f6f2fdf1be57f3e2cce0612e743d3f6b51341a740903"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("doc/obfs4proxy.1")
