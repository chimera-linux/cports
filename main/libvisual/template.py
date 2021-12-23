pkgname = "libvisual"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
# must be used to overwrite generated junk that messes up build
make_dir = "."
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Abstraction library for audio visualization plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://sourceforge.net/projects/libvisual"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "0b4dfdb87125e129567752089e3c8b54cefed601eef169d2533d8659da8dc1d7"

@subpackage("libvisual-devel")
def _devel(self):
    return self.default_devel()
