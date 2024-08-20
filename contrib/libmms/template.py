pkgname = "libmms"
pkgver = "0.6.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["glib-devel"]
pkgdesc = "MMS stream protocol library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://sourceforge.net/projects/libmms"
source = f"$(SOURCEFORGE_SITE)/libmms/libmms-{pkgver}.tar.gz"
sha256 = "3c05e05aebcbfcc044d9e8c2d4646cd8359be39a3f0ba8ce4e72a9094bee704f"


@subpackage("libmms-devel")
def _(self):
    return self.default_devel()
