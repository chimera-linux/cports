pkgname = "libmwaw"
pkgver = "0.3.22"
pkgrel = 7
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["librevenge-devel", "boost-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library for importing legacy Mac documents"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://sourceforge.net/projects/libmwaw"
source = f"$(SOURCEFORGE_SITE)/libmwaw/libmwaw-{pkgver}.tar.xz"
sha256 = "a1a39ffcea3ff2a7a7aae0c23877ddf4918b554bf82b0de5d7ce8e7f61ea8e32"


@subpackage("libmwaw-progs")
def _(self):
    return self.default_progs()


@subpackage("libmwaw-devel")
def _(self):
    return self.default_devel()
