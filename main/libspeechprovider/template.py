pkgname = "libspeechprovider"
pkgver = "1.0.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = ["glib-devel"]
checkdepends = ["python-gobject", "python-tap.py"]
pkgdesc = "Speech provider resources"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://project-spiel.org"
source = f"https://github.com/project-spiel/libspeechprovider/archive/refs/tags/SPEECHPROVIDER_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "e83e32428cd8b684dff3c931601151d1202e0b6370990a605a36322804959cae"


@subpackage("libspeechprovider-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
