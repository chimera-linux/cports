pkgname = "libvisual"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-examples"]
make_cmd = "gmake"
# must be used to overwrite generated junk that messes up build
make_dir = "."
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Abstraction library for audio visualization plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://sourceforge.net/projects/libvisual"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "aa12877417f76d3642d9f4c723302380d833175639d63a55641d01928a5ddb7d"


@subpackage("libvisual-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
