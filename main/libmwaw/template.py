pkgname = "libmwaw"
pkgver = "0.3.23"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["librevenge-devel", "boost-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library for importing legacy Mac documents"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://sourceforge.net/projects/libmwaw"
source = f"$(SOURCEFORGE_SITE)/libmwaw/libmwaw-{pkgver}.tar.xz"
sha256 = "ac3590f691a2904eb8c7dc8b757b8a29f125f592449e421459ae8fa928b399eb"


@subpackage("libmwaw-progs")
def _(self):
    return self.default_progs()


@subpackage("libmwaw-devel")
def _(self):
    return self.default_devel()
