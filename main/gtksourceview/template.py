pkgname = "gtksourceview"
pkgver = "5.14.1"
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
sha256 = "009862e87b929da5a724ece079f01f8cee29e74797a1ecac349f58c15a3cbc58"
# FIXME: lto results in broken mouse scrolling in gnome-text-editor
# also seems to have a weird pango interaction; the tests sigill if only both
# have lto
options = ["!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _(self):
    return self.default_devel()
