pkgname = "libmicrodns"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Minimal mDNS resolver library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/videolabs/libmicrodns"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9864a088ffef4d4255d5abf63c6f603d1dc343dfec2809ff0c3f1624045b80fa"


@subpackage("libmicrodns-devel")
def _devel(self):
    return self.default_devel()
