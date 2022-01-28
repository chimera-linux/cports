pkgname = "libpeas"
pkgver = "1.30.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddemos=false", "-Dvapi=true"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala",
    "gobject-introspection", "python"
]
makedepends = [
    "libglib-devel", "python-devel", "python-gobject-devel", "gtk+3-devel",
    "glade3-devel"
]
depends = ["python-gobject", "hicolor-icon-theme"]
pkgdesc = "G0bject application plugin library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Libpeas"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0bf5562e9bfc0382a9dcb81f64340787542568762a3a367d9d90f6185898b9a3"
# no xvfb-run
options = ["!check"]

@subpackage("libpeas-devel")
def _devel(self):
    return self.default_devel()
