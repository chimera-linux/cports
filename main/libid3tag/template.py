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
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for reading ID3 metadata tags from MP3 files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
# this is the slightly updated forked version
url = "https://codeberg.org/tenacityteam/libid3tag"
source = f"https://codeberg.org/tenacityteam/libid3tag/archive/{pkgver}.tar.gz"
sha256 = "0561009778513a95d91dac33cee8418d6622f710450a7cb56a74636d53b588cb"
# vis breaks symbols
hardening = []


@subpackage("libid3tag-devel")
def _(self):
    return self.default_devel()
