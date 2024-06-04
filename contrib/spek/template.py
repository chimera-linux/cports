pkgname = "spek"
pkgver = "0.8.5"
pkgrel = 1
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "wxwidgets-devel",
]
pkgdesc = "Acoustic spectrum analyser"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-only"
url = "https://github.com/alexkay/spek"
source = f"{url}/releases/download/v{pkgver}/spek-{pkgver}.tar.xz"
sha256 = "1bccf85a14a01af8f2f30476cbad004e8bf6031f500e562bbe5bbd1e5eb16c59"
hardening = ["vis", "cfi"]
