pkgname = "sane-airscan"
pkgver = "0.99.33"
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
license = "GPL-2.0-or-later WITH SANE-exception"
url = "https://github.com/alexpevzner/sane-airscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "647f41f84f9bce743c796ca84c1fda67e519968fab407490c28fd0cc6d7ac485"
