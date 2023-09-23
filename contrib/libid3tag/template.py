pkgname = "libid3tag"
pkgver = "0.16.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "zlib-devel",
]
pkgdesc = "Library for reading ID3 metadata tags from MP3 files"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
# this is the slightly updated forked version
url = "https://codeberg.org/tenacityteam/libid3tag"
source = f"https://codeberg.org/tenacityteam/libid3tag/archive/{pkgver}.tar.gz"
sha256 = "8cebfba0a7cdf4fada8b715fc17a29ddadd825448da05db006e18acd8bc2731d"
# vis breaks symbols
hardening = []


@subpackage("libid3tag-devel")
def _devel(self):
    return self.default_devel()
