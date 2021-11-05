pkgname = "harfbuzz"
pkgver = "2.9.1"
pkgrel = 0
build_style = "meson"
# FIXME: introspection, docs
configure_args = [
    "-Dglib=enabled",
    "-Dfreetype=enabled",
    "-Dcairo=enabled",
    "-Dicu=enabled",
    "-Dgraphite=enabled",
    "-Dintrospection=disabled",
    "-Ddocs=disabled",
]
hostmakedepends = ["meson", "pkgconf", "glib-devel"]
makedepends = ["cairo-devel", "graphite2-devel", "icu-devel"]
pkgdesc = "Text shaping engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0edcc980f526a338452180e701d6aba6323aef457b6686976a7d17ccbddc51cf"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libharfbuzz")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()
