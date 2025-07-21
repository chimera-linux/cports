pkgname = "gtksourceview"
pkgver = "5.16.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dintrospection=enabled", "-Dvapi=true"]
make_check_wrapper = ["dbus-run-session", "wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pcre2-devel",
    "pkgconf",
    "vala",
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
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GtkSourceView"
source = (
    f"$(GNOME_SITE)/gtksourceview/{pkgver[:-2]}/gtksourceview-{pkgver}.tar.xz"
)
sha256 = "ab35d420102f3e8b055dd3b8642d3a48209f888189e6254d0ffb4b6a7e8c3566"
# FIXME: lto results in broken mouse scrolling in gnome-text-editor
# also seems to have a weird pango interaction; the tests sigill if only both
# have lto
options = ["!cross", "!lto"]


@subpackage("gtksourceview-devel")
def _(self):
    return self.default_devel()
