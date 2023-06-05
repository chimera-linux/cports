pkgname = "liblangtag"
pkgver = "0.6.4"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf",
    "gmake",
    "automake",
    "libtool",
    "gobject-introspection",
    "gtk-doc-tools",
]
makedepends = ["libxml2-devel"]
pkgdesc = "Interface library to access tags for identifying languages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0 OR LGPL-3.0-or-later"
url = "https://bitbucket.org/tagoh/liblangtag"
source = f"{url}/downloads/{pkgname}-{pkgver}.tar.bz2"
sha256 = "5701062c17d3e73ddaa49956cbfa5d47d2f8221988dec561c0af2118c1c8a564"


@subpackage("liblangtag-devel")
def _devel(self):
    return self.default_devel()
