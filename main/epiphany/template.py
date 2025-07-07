pkgname = "epiphany"
pkgver = "48.5"
pkgrel = 1
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
sha256 = "0f66552ad6593c7952a3ddee5bf515656c8c434871076d9f1a91a7af9346b1b4"
