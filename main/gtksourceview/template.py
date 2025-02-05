pkgname = "gtksourceview"
pkgver = "5.14.2"
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
    "libxslt-progs",
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
sha256 = "1a6d387a68075f8aefd4e752cf487177c4a6823b14ff8a434986858aeaef6264"
# FIXME: lto results in broken mouse scrolling in gnome-text-editor
# also seems to have a weird pango interaction; the tests sigill if only both
# have lto
options = ["!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _(self):
    return self.default_devel()
