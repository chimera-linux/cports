pkgname = "eog"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "exempi-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gtk+3-devel",
    "lcms2-devel",
    "libexif-devel",
    "libhandy-devel",
    "libjpeg-turbo-devel",
    "libpeas-devel",
    "libportal-devel",
    "librsvg-devel",
]
depends = ["shared-mime-info"]
provides = ["so:libeog.so=0"]
pkgdesc = "GNOME image viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/EyeOfGnome"
source = f"$(GNOME_SITE)/eog/{pkgver[:-2]}/eog-{pkgver}.tar.xz"
sha256 = "db5edbf5224d75126a7b7d8ee4e9272a2f30a953331d5baf6d3f3c0ce0cbde66"
options = ["!cross"]


@subpackage("eog-devel")
def _(self):
    return self.default_devel()
