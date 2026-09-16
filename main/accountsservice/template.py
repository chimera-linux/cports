pkgname = "accountsservice"
pkgver = "26.27.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemdsystemunitdir=no",
    "-Dintrospection=true",
    "-Delogind=true",
    "-Dtests=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "polkit",
    "vala",
]
makedepends = ["json-c-devel", "polkit-devel", "elogind-devel", "dbus-devel"]
checkdepends = ["python-dbus"]
pkgdesc = "D-Bus service for accessing user accounts"
license = "GPL-3.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/AccountsService"
source = f"https://gitlab.freedesktop.org/accountsservice/accountsservice/-/archive/{pkgver}/accountsservice-{pkgver}.tar.gz"
sha256 = "11de07bcd499c2277f78a6fc830d1437654f3397cc7bbed19c28b3818435ba38"
# does not like the dbusmock for some reason
options = ["!cross", "!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("accountsservice-devel")
def _(self):
    return self.default_devel()
