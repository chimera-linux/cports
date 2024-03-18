pkgname = "eog"
pkgver = "45.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext",
    "itstool",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "libpeas-devel",
    "gnome-desktop-devel",
    "gdk-pixbuf-devel",
    "libexif-devel",
    "exempi-devel",
    "lcms2-devel",
    "libportal-devel",
    "librsvg-devel",
    "libjpeg-turbo-devel",
]
depends = ["shared-mime-info"]
provides = ["so:libeog.so=0"]
pkgdesc = "GNOME image viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/EyeOfGnome"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8650f662d4921d83a7904f6bb9ca245baf735f717b47fac5b37f0d90e5e891a8"
options = ["!cross"]


@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
