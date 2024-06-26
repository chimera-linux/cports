pkgname = "gtksourceview"
pkgver = "5.12.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dvapi=true"]
make_check_wrapper = ["dbus-run-session", "wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pcre2-devel",
    "pkgconf",
    "vala",
    "xsltproc",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libxml2-devel",
    "pcre2-devel",
    "vala",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "Advanced Gtk4 text editor widget"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GtkSourceView"
source = (
    f"$(GNOME_SITE)/gtksourceview/{pkgver[:-2]}/gtksourceview-{pkgver}.tar.xz"
)
sha256 = "84c82aad985c5aadae7cea7804904a76341ec82b268d46594c1a478f39b42c1f"
# lto results in broken mouse scrolling in gnome-text-editor
options = ["!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _devel(self):
    return self.default_devel()
