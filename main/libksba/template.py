pkgname = "libksba"
pkgver = "1.6.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "CMS and X.509 access library"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://gnupg.org/software/libksba/index.html"
source = f"https://gnupg.org/ftp/gcrypt/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "a564628c574c99287998753f98d750babd91a4e9db451f46ad140466ef2a6d16"


@subpackage("libksba-devel")
def _devel(self):
    return self.default_devel()
