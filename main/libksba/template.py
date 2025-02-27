pkgname = "libksba"
pkgver = "1.6.7"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "CMS and X.509 access library"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://gnupg.org/software/libksba/index.html"
source = f"https://gnupg.org/ftp/gcrypt/libksba/libksba-{pkgver}.tar.bz2"
sha256 = "cf72510b8ebb4eb6693eef765749d83677a03c79291a311040a5bfd79baab763"


@subpackage("libksba-devel")
def _(self):
    return self.default_devel()
