pkgname = "lrdf"
pkgver = "0.6.1"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."  # tests assume this build directory
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["raptor-devel", "ladspa-sdk"]
pkgdesc = "RDF library with special support for LADSPA plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/swh/LRDF"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d579417c477ac3635844cd1b94f273ee2529a8c3b6b21f9b09d15f462b89b1ef"


@subpackage("lrdf-devel")
def _devel(self):
    self.depends += ["raptor-devel"]

    return self.default_devel()
