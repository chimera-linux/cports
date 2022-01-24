pkgname = "accountsservice"
pkgver = "0.6.55"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemdsystemunitdir=no", "-Dintrospection=true", "-Delogind=true",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "polkit"
]
makedepends = ["polkit-devel", "elogind-devel", "dbus-devel"]
pkgdesc = "D-Bus service for accessing user accounts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/AccountsService"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ff2b2419a7e06bd9cb335ffe391c7409b49a0f0130b890bd54692a3986699c9b"

def post_install(self):
    self.install_dir("var/lib/AccountsService/users", empty = True)
    self.install_dir("var/lib/AccountsService/icons", empty = True)

@subpackage("accountsservice-devel")
def _devel(self):
    return self.default_devel()
