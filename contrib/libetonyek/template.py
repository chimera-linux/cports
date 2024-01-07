pkgname = "libetonyek"
pkgver = "0.1.10"
pkgrel = 2
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = [
    "librevenge-devel",
    "boost-devel",
    "libxml2-devel",
    "liblangtag-devel",
    "glm",
    "mdds",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "Library for Apple Keynote presentations"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libetonyek"
source = (
    f"https://dev-www.libreoffice.org/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "b430435a6e8487888b761dc848b7981626eb814884963ffe25eb26a139301e9a"


def init_configure(self):
    for f in (self.bldroot_path / "usr/include").glob("mdds-*"):
        self.configure_args += ["--with-mdds=" + f.name.removeprefix("mdds-")]


@subpackage("libetonyek-progs")
def _progs(self):
    return self.default_progs()


@subpackage("libetonyek-devel")
def _devel(self):
    return self.default_devel()
