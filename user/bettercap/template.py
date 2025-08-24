pkgname = "bettercap"
pkgver = "2.41.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["libnetfilter_queue-devel", "libpcap-devel", "libusb-devel"]
pkgdesc = "Swiss Army knife for network attacks"
license = "GPL-3.0-only"
url = "https://bettercap.org"
source = (
    f"https://github.com/bettercap/bettercap/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c00a489110a01b799796bfc5701bbaea882e0a1aa675d16ce2aba25bd0d71ad1"


# make sure cgo is enabled while cross-compiling
def init_build(self):
    from cbuild.util import golang

    self.env["CGO_ENABLED"] = "1"
    self.env.update(golang.get_go_env(self))
