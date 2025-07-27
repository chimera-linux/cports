pkgname = "sane-airscan"
pkgver = "0.99.36"
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
sha256 = "43d3436c0199496ee18aca4f875fe3926a40a0fae781bc280cdb96f7b5068ac0"
