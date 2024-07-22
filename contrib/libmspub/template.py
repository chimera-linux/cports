pkgname = "libmspub"
pkgver = "0.1.4"
pkgrel = 5
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "icu-devel",
    "librevenge-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for mspub format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libmspub"
source = (
    f"https://dev-www.libreoffice.org/src/libmspub/libmspub-{pkgver}.tar.xz"
)
sha256 = "ef36c1a1aabb2ba3b0bedaaafe717bf4480be2ba8de6f3894be5fd3702b013ba"

tool_flags = {"CXXFLAGS": ["-D_HAS_AUTO_PTR_ETC=0"]}


@subpackage("libmspub-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libmspub-devel")
def _devel(self):
    return self.default_devel()
