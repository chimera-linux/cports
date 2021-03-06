pkgname = "epiphany"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunit_tests=disabled", "-Dsoup2=disabled"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext-tiny", "itstool"]
makedepends = [
    "webkitgtk-devel", "cairo-devel", "gcr-devel", "gdk-pixbuf-devel",
    "libglib-devel", "gsettings-desktop-schemas-devel", "gtk+3-devel",
    "nettle-devel", "json-glib-devel", "libarchive-devel", "libdazzle-devel",
    "libhandy-devel", "libsecret-devel", "libxml2-devel", "libportal-devel",
    "libsoup-devel", "sqlite-devel", "gmp-devel", "iso-codes",
]
depends = ["hicolor-icon-theme", "iso-codes"]
pkgdesc = "GNOME web browser"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Web"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3dbfa8c00e45b7f44e1824d01f0febe83707b5fb9330c261173f68b7f03cd5e3"
