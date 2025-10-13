pkgname = "libetonyek"
pkgver = "0.1.13"
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
    "glm",
    "liblangtag-devel",
    "librevenge-devel",
    "libxml2-devel",
    "mdds",
]
checkdepends = ["cppunit-devel"]
pkgdesc = "Library for Apple Keynote presentations"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libetonyek"
source = (
    f"https://dev-www.libreoffice.org/src/libetonyek/libetonyek-{pkgver}.tar.xz"
)
sha256 = "032b71cb597edd92a0b270b916188281bc35be55296b263f6817b29adbcb1709"


def init_configure(self):
    for f in (self.bldroot_path / "usr/include").glob("mdds-*"):
        self.configure_args += ["--with-mdds=" + f.name.removeprefix("mdds-")]


@subpackage("libetonyek-progs")
def _(self):
    return self.default_progs()


@subpackage("libetonyek-devel")
def _(self):
    return self.default_devel()
