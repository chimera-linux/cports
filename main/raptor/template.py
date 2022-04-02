pkgname = "raptor"
pkgver = "2.0.15"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-yajl=no"]
make_check_args = ["-j1"] # racey tests
hostmakedepends = ["pkgconf"]
makedepends = [
    "libcurl-devel", "libxml2-devel", "libxslt-devel", "icu-devel",
    "zlib-devel", "liblzma-devel"
]
pkgdesc = "Raptor RDF syntax library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 OR LGPL-2.1-or-later OR GPL-2.0-or-later"
url = "https://librdf.org/raptor"
source = f"https://librdf.org/dist/source/raptor2-{pkgver}.tar.gz"
sha256 = "ada7f0ba54787b33485d090d3d2680533520cd4426d2f7fb4782dd4a6a1480ed"

@subpackage("raptor-devel")
def _devel(self):
    # Requires are not listed
    self.depends += makedepends

    return self.default_devel()

@subpackage("raptor-progs")
def _progs(self):
    return self.default_progs()
