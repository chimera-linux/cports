pkgname = "eog"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "gettext-tiny",
    "itstool",
]
makedepends = [
    "glib-devel", "gtk+3-devel", "libhandy-devel", "libpeas-devel",
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
sha256 = "41d85fab05c430898dbfd847e48e1f5b4935dc3cbcee546e759a907eda671054"
options = ["!cross"]

@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
