pkgname = "gpgme-qt"
# update main/gpgme too
pkgver = "1.23.2"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-languages=cpp qt6",
]
# otherwise cmake files are broken
hostmakedepends = [
    "automake",
    "gnupg",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gpgme-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "qt6-qtbase-devel",
]
depends = ["gnupg"]
origin = "gpgme"
pkgdesc = "Qt support for gpgme library"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgme/gpgme-{pkgver}.tar.bz2"
sha256 = "9499e8b1f33cccb6815527a1bc16049d35a6198a6c5fae0185f2bd561bce5224"


def post_install(self):
    self.uninstall("usr/bin")
    self.uninstall("usr/include/gpgme++")
    self.uninstall("usr/include/gpgme.h")
    self.uninstall("usr/lib/cmake/Gpgmepp")
    self.uninstall("usr/lib/libgpg*", glob=True)
    self.uninstall("usr/lib/pkgconfig")
    self.uninstall("usr/share")


@subpackage("gpgme-qt-devel")
def _(self):
    self.depends += ["gpgme-devel"]
    return self.default_devel()
