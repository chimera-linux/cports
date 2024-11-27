pkgname = "libaccounts-glib"
pkgver = "1.27"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "check-devel",
    "glib-devel",
    "libxml2-devel",
    "sqlite-devel",
]
checkdepends = ["dbus"]
pkgdesc = "GLib-based library for managing the accounts database"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://gitlab.com/accounts-sso/libaccounts-glib"
source = (
    f"{url}/-/archive/VERSION_{pkgver}/libaccounts-glib-VERSION_{pkgver}.tar.gz"
)
sha256 = "a8407a5897a2e425ea1aa955ecf88485dd2fd417919de275b27c781a5d0637a5"
# gobject-introspection
options = ["!cross"]


@subpackage("libaccounts-glib-devel")
def _(self):
    return self.default_devel()
