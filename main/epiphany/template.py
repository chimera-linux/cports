pkgname = "epiphany"
pkgver = "48.3"
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
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Web"
source = (
    f"$(GNOME_SITE)/epiphany/{pkgver.split('.')[0]}/epiphany-{pkgver}.tar.xz"
)
sha256 = "da2953e7e2b73bf7473c0a33979104d79362795295eaa0a2a38ea188537daf13"
