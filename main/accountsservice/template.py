pkgname = "accountsservice"
pkgver = "23.13.9"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dsystemdsystemunitdir=no",
    "-Dintrospection=true",
    "-Delogind=true",
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
makedepends = ["polkit-devel", "elogind-devel", "dbus-devel"]
checkdepends = ["python-dbus"]
pkgdesc = "D-Bus service for accessing user accounts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/AccountsService"
source = f"$(FREEDESKTOP_SITE)/accountsservice/accountsservice-{pkgver}.tar.xz"
sha256 = "adda4cdeae24fa0992e7df3ffff9effa7090be3ac233a3edfdf69d5a9c9b924f"
# does not like the dbusmock for some reason
options = ["!cross", "!check"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("accountsservice-devel")
def _(self):
    return self.default_devel()
