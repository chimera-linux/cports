pkgname = "libksba"
pkgver = "1.8.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libgpg-error-devel"]
pkgdesc = "CMS and X.509 access library"
license = "GPL-2.0-or-later OR LGPL-3.0-or-later"
url = "https://gnupg.org/software/libksba/index.html"
source = f"https://gnupg.org/ftp/gcrypt/libksba/libksba-{pkgver}.tar.bz2"
sha256 = "c2f84393011827219ae117131dba8e7684c2bed0961eed11b0642c2acba440b5"


@subpackage("libksba-devel")
def _(self):
    return self.default_devel()
