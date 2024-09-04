pkgname = "eog"
pkgver = "47_beta"
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
source = f"$(GNOME_SITE)/eog/{pkgver[:2]}/eog-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "5ce2f230032497e9c4bd1ec05a6f5f18c61567b58cc8033b1a7e48b09a8a0e27"
options = ["!cross"]


@subpackage("eog-devel")
def _(self):
    return self.default_devel()
