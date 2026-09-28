pkgname = "gpgmepp"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["gpgme-devel", "libgpg-error-devel"]
pkgdesc = "C++ bindings for gpgme"
license = "LGPL-2.0-or-later"
url = "https://gnupg.org/software/gpgme/index.html"
source = f"https://gnupg.org/ftp/gcrypt/gpgmepp/gpgmepp-{pkgver}.tar.xz"
sha256 = "d4796049c06708a26f3096f748ef095347e1a3c1e570561701fe952c3f565382"


@subpackage("gpgmepp-devel")
def _(self):
    return self.default_devel()
