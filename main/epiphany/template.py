pkgname = "epiphany"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunit_tests=disabled"]
hostmakedepends = [
    "blueprint-compiler",
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
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Web"
source = (
    f"$(GNOME_SITE)/epiphany/{pkgver.split('.')[0]}/epiphany-{pkgver}.tar.xz"
)
sha256 = "271ec735b9836b97449e32793d354a8afb6b9f8d2d3d75821885d5e155707929"
