pkgname = "dpkg"
pkgver = "1.22.11"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gpatch",
    "gtar",
    "libtool",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "libmd-devel",
    "ncurses-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = [
    "fakeroot",
    "gnupg",
]
pkgdesc = "Debian package manager"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://wiki.debian.org/Teams/Dpkg"
source = f"https://deb.debian.org/debian/pool/main/d/dpkg/dpkg_{pkgver}.tar.xz"
sha256 = "f318eb949b8e7ecd802b17b1a7e7cf4b17094c9577e1060653e9b838cdd31d80"


@subpackage("dpkg-devel")
def _devel(self):
    return self.default_devel()
