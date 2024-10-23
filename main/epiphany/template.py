pkgname = "epiphany"
pkgver = "47.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunit_tests=disabled"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gcr-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gmp-devel",
    "gsettings-desktop-schemas-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "iso-codes",
    "json-glib-devel",
    "libadwaita-devel",
    "libarchive-devel",
    "libportal-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libxml2-devel",
    "nettle-devel",
    "sqlite-devel",
    "webkitgtk4-devel",
]
depends = ["iso-codes"]
pkgdesc = "GNOME web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Web"
source = f"$(GNOME_SITE)/epiphany/{pkgver[:-2]}/epiphany-{pkgver}.tar.xz"
sha256 = "34dafd8363a098b44d476e2e9823b4cbea6e66afad33bba10ed7a13ff1a964f1"
