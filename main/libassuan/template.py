pkgname = "libassuan"
pkgver = "3.0.1"
pkgrel = 0
build_style = "gnu_configure"
# their autoconf is dumb
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "IPC library used by some GnuPG related software"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org/related_software/libassuan"
source = f"https://gnupg.org/ftp/gcrypt/libassuan/libassuan-{pkgver}.tar.bz2"
sha256 = "c8f0f42e6103dea4b1a6a483cb556654e97302c7465308f58363778f95f194b1"


@subpackage("libassuan-devel")
def _(self):
    return self.default_devel()
