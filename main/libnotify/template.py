pkgname = "libnotify"
pkgver = "0.8.7"
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
sha256 = "4be15202ec4184fce1ac15997ece5530d2be32fe9573875aeb10e3b573858748"
# cross: introspection
# check: cycle with xwayland-run
options = ["!cross", "!check"]


@subpackage("libnotify-devel")
def _(self):
    return self.default_devel()
