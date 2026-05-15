pkgname = "libnotify"
pkgver = "0.8.8"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dintrospection=enabled",
    "-Ddocbook_docs=disabled",
    "-Dgtk_doc=false",
]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "docbook-xsl",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "gdk-pixbuf-devel",
    "glib-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "libpng-devel",
]
checkdepends = ["xwayland-run", "dbus"]
pkgdesc = "Desktop notification library"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libnotify"
source = f"$(GNOME_SITE)/libnotify/{pkgver[:-2]}/libnotify-{pkgver}.tar.xz"
sha256 = "23420ef619dc2cb5aebad613f4823a2fa41c07e5a1d05628d40f6ec4b35bfddd"
# cross: introspection
# check: cycle with xwayland-run
options = ["!cross", "!check"]


@subpackage("libnotify-devel")
def _(self):
    return self.default_devel()
