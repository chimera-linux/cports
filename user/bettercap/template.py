pkgname = "bettercap"
pkgver = "2.41.7"
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
sha256 = "797274ac3a4e35e40e640958c267a60f559213d9ae1322ab721d8f4ec71cbaeb"
env = {"CGO_ENABLED": "1"}
