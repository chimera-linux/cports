pkgname = "libmspub"
pkgver = "0.1.4"
pkgrel = 12
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "icu-devel",
    "librevenge-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Library for mspub format"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libmspub"
source = (
    f"https://dev-www.libreoffice.org/src/libmspub/libmspub-{pkgver}.tar.xz"
)
sha256 = "ef36c1a1aabb2ba3b0bedaaafe717bf4480be2ba8de6f3894be5fd3702b013ba"

tool_flags = {"CXXFLAGS": ["-D_HAS_AUTO_PTR_ETC=0"]}


@subpackage("libmspub-progs")
def _(self):
    return self.default_progs()


@subpackage("libmspub-devel")
def _(self):
    return self.default_devel()
