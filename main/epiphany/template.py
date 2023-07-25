pkgname = "epiphany"
pkgver = "44.5"
pkgrel = 1
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
depends = ["desktop-file-utils", "iso-codes"]
pkgdesc = "GNOME web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Web"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3c475e04ed2a0f410cb44b96937563697079193ac9b7a50c91485fb9b08315ab"
