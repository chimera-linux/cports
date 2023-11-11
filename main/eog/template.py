pkgname = "eog"
pkgver = "45.1"
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
depends = ["desktop-file-utils", "shared-mime-info"]
provides = ["so:libeog.so=0"]
pkgdesc = "GNOME image viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/EyeOfGnome"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c17f86704c722b36c01a168f1e51439be0bb279f2c6646f48b66e9d0f3a24cd2"
options = ["!cross"]


@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
