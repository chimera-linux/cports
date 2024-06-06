pkgname = "gpgme-qt"
# update main/gpgme too
pkgver = "1.23.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-languages=cpp qt6",
]
# otherwise cmake files are broken
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
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
pkgdesc = "GnuPG Made Easy (Qt library)"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgme/gpgme-{pkgver}.tar.bz2"
sha256 = "9499e8b1f33cccb6815527a1bc16049d35a6198a6c5fae0185f2bd561bce5224"


def post_install(self):
    self.rm(self.destdir / "usr/bin", recursive=True)
    self.rm(self.destdir / "usr/include/gpgme++", recursive=True)
    self.rm(self.destdir / "usr/include/gpgme.h")
    self.rm(self.destdir / "usr/lib/cmake/Gpgmepp", recursive=True)
    self.rm(self.destdir / "usr/lib/libgpg*", glob=True)
    self.rm(self.destdir / "usr/lib/pkgconfig", recursive=True)
    self.rm(self.destdir / "usr/share", recursive=True)


@subpackage("gpgme-qt-devel")
def _devel(self):
    self.depends += ["gpgme-devel"]
    return self.default_devel()
