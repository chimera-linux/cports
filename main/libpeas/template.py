pkgname = "libpeas"
pkgver = "1.32.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddemos=false", "-Dvapi=true"]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala",
    "gobject-introspection", "python"
]
makedepends = [
    "libglib-devel", "python-devel", "python-gobject-devel", "gtk+3-devel",
    "glade3-devel"
]
depends = ["python-gobject", "hicolor-icon-theme"]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "G0bject application plugin library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Libpeas"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d625520fa02e8977029b246ae439bc218968965f1e82d612208b713f1dcc3d0e"
options = ["!cross"]

@subpackage("libpeas-devel")
def _devel(self):
    return self.default_devel()
