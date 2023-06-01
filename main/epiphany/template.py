pkgname = "epiphany"
pkgver = "44.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunit_tests=disabled"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext-tiny",
    "itstool",
    "desktop-file-utils",
]
makedepends = [
    "webkitgtk4-devel",
    "cairo-devel",
    "gcr-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "gstreamer-devel",
    "nettle-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libadwaita-devel",
    "libsecret-devel",
    "libxml2-devel",
    "libportal-devel",
    "libsoup-devel",
    "sqlite-devel",
    "gmp-devel",
    "iso-codes",
]
depends = ["hicolor-icon-theme", "iso-codes"]
pkgdesc = "GNOME web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Web"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f5e904b2e5102104d8b7fe3a615034add78de03116492b54cbdebca280bdd899"
