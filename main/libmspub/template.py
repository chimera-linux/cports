pkgname = "libmspub"
pkgver = "0.1.5"
pkgrel = 0
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
sha256 = "3671095f5a10bee8a755052a30576952c5b16d8b0f2ba9f2fb998338c18cb119"

tool_flags = {"CXXFLAGS": ["-D_HAS_AUTO_PTR_ETC=0"]}


@subpackage("libmspub-progs")
def _(self):
    return self.default_progs()


@subpackage("libmspub-devel")
def _(self):
    return self.default_devel()
