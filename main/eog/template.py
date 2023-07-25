pkgname = "eog"
pkgver = "44.3"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "gettext-tiny",
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
sha256 = "d6b2d70f4b432ff8cf494c8f9029b2621d08e7817938317d64063ae6c4da9d8c"
options = ["!cross"]


@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
