pkgname = "libid3tag"
pkgver = "0.16.2"
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
sha256 = "02721346d554c4b4aa3966b134152be65eb4df1fb9322d2d019133238d2ba017"
# vis breaks symbols
hardening = []


@subpackage("libid3tag-devel")
def _devel(self):
    return self.default_devel()
