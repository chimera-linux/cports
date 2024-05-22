pkgname = "sane-airscan"
pkgver = "0.99.29"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later WITH SANE-exception"
url = "https://github.com/alexpevzner/sane-airscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e8aa43005ed495fc0db65e2ff51b29cef11a45fc6d8c385294b3394b848db65f"
