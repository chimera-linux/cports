pkgname = "liblangtag"
pkgver = "0.6.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["libxml2-devel"]
pkgdesc = "Interface library to access tags for identifying languages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-3.0-or-later"
url = "https://bitbucket.org/tagoh/liblangtag"
source = f"{url}/downloads/liblangtag-{pkgver}.tar.bz2"
sha256 = "5ed6bcd4ae3f3c05c912e62f216cd1a44123846147f729a49fb5668da51e030e"


@subpackage("liblangtag-devel")
def _(self):
    return self.default_devel()
