pkgname = "eog"
pkgver = "42.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "gettext-tiny",
    "itstool",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "libhandy-devel", "libpeas-devel",
    "gnome-desktop-devel", "gdk-pixbuf-devel", "libexif-devel",
    "exempi-devel", "lcms2-devel", "libportal-devel", "librsvg-devel",
    "libjpeg-turbo-devel",
]
depends = ["hicolor-icon-theme", "shared-mime-info"]
provides = ["so:libeog.so=0"]
pkgdesc = "GNOME image viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/EyeOfGnome"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "30c1b3c28bc6dc2854d878ebd31a22eaa15bf959c134206a2a1904193e47f43a"
options = ["!cross"]

@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
