pkgname = "sane-airscan"
pkgver = "0.99.30"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "avahi-devel",
    "gnutls-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "libxml2-devel",
    "linux-headers",
    "sane-backends-devel",
]
pkgdesc = "SANE backend for AirScan (eSCL) and WSD document scanners"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later WITH SANE-exception"
url = "https://github.com/alexpevzner/sane-airscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "89bef46839b5f07689f29e9550b694748d70263cbd66a34566e7d616ca228ad6"
