pkgname = "sane-airscan"
pkgver = "0.99.31"
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
sha256 = "67782be6a4fd36e753fc4766b8989d75f806bc6d1d2e92f617ea686be2924c14"
