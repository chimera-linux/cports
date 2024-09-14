pkgname = "gtksourceview"
pkgver = "5.14.0"
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
sha256 = "c40d1f7309d111f5805fec47c1fead519c4b8d506317ce5e90013ce47d65e9c6"
# FIXME: lto results in broken mouse scrolling in gnome-text-editor
# also seems to have a weird pango interaction; the tests sigill if only both
# have lto
options = ["!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _(self):
    return self.default_devel()
