pkgname = "libmspub"
pkgver = "0.1.4"
pkgrel = 3
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["librevenge-devel", "boost-devel", "icu-devel", "zlib-devel"]
pkgdesc = "Library for mspub format"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libmspub"
source = (
    f"https://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "ef36c1a1aabb2ba3b0bedaaafe717bf4480be2ba8de6f3894be5fd3702b013ba"

tool_flags = {"CXXFLAGS": ["-D_HAS_AUTO_PTR_ETC=0"]}


@subpackage("libmspub-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libmspub-devel")
def _devel(self):
    return self.default_devel()
