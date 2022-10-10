pkgname = "vte3"
pkgver = "0.70.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=false", "-D_systemd=false", "-Dgir=true", "-Dvapi=true",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny-devel", "gperf",
    "gobject-introspection", "vala", "bash",
]
makedepends = [
    "libglib-devel", "gnutls-devel", "gtk+3-devel", "pcre2-devel",
    "vala-devel", "pango-devel", "fribidi-devel", "icu-devel",
    "zlib-devel", "linux-headers",
]
pkgdesc = "Gtk+3 terminal widget"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal/VTE"
source = f"$(GNOME_SITE)/vte/{pkgver[:-2]}/vte-{pkgver}.tar.xz"
sha256 = "93e0dd4a1bc2a7a1a62da64160a274cce456976ea1567d98591da96e2d265ae6"
# assert in meson
options = ["!lto", "!cross"]

@subpackage("vte3-devel")
def _devel(self):
    return self.default_devel()
