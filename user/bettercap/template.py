pkgname = "bettercap"
pkgver = "2.41.5"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["libnetfilter_queue-devel", "libpcap-devel", "libusb-devel"]
pkgdesc = "Swiss Army knife for network attacks"
license = "GPL-3.0-only"
url = "https://bettercap.org"
source = (
    f"https://github.com/bettercap/bettercap/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "85513871e105a182eb92f80ba9563ac37cb8a48bcfa98d30e1197e74c42ff15a"
env = {"CGO_ENABLED": "1"}
