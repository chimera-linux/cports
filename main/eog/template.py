pkgname = "eog"
pkgver = "43.1"
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
sha256 = "fed79ff3ca19bac62f27155c9bdd69eef875870b971e6dcb0aa38c093d131971"
# glib
hardening = ["!vis"]
options = ["!cross"]

@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
