pkgname = "bettercap"
pkgver = "2.41.4"
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
sha256 = "384848630f594fadd48e80406f4cf8ceccfe3f32dd9182f7e18c20240e74a5fd"
env = {"CGO_ENABLED": "1"}
