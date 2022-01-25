pkgname = "vte3"
pkgver = "0.66.2"
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
sha256 = "e89974673a72a0a06edac6d17830b82bb124decf0cb3b52cebc92ec3ff04d976"
# assert in meson
options = ["!lto"]

@subpackage("vte3-devel")
def _devel(self):
    return self.default_devel()
