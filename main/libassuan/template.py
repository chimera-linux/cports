pkgname = "libassuan"
pkgver = "3.0.2"
pkgrel = 0
build_style = "gnu_configure"
# their autoconf is dumb
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "IPC library used by some GnuPG related software"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org/related_software/libassuan"
source = f"https://gnupg.org/ftp/gcrypt/libassuan/libassuan-{pkgver}.tar.bz2"
sha256 = "d2931cdad266e633510f9970e1a2f346055e351bb19f9b78912475b8074c36f6"


@subpackage("libassuan-devel")
def _(self):
    return self.default_devel()
