pkgname = "qgpgme"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gpgmepp-devel", "libgpg-error-devel", "qt6-qtbase-devel"]
renames = ["gpgme-qt"]
pkgdesc = "Qt bindings for gpgme"
license = "GPL-2.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/qgpgme/qgpgme-{pkgver}.tar.xz"
sha256 = "15645b2475cca6118eb2ed331b3a8d9442c9d4019c3846ba3f6d25321b4a61ad"


@subpackage("qgpgme-devel")
def _(self):
    self.renames = ["gpgme-qt-devel"]
    self.depends = ["gpgmepp-devel"]

    return self.default_devel()
