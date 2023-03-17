pkgname = "eog"
pkgver = "43.2"
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
sha256 = "9dcfdce5585a90e2bb1cf57e377cb1eb12d41bd9bcb9bbacdf506bc1b1354ef9"
options = ["!cross"]

@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
