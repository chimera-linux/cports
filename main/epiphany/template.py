pkgname = "epiphany"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dunit_tests=disabled"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "itstool",
    "desktop-file-utils",
]
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
sha256 = "b66d499f9ee72696d83cf844125377181a954554a4bb3785b73293380ac0c227"
