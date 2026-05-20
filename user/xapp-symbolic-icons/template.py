pkgname = "xapp-symbolic-icons"
pkgver = "1.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Set of symbolic icons for Gtk applications and projects"
license = "LGPL-3.0-or-later"
url = "https://github.com/xapp-project/xapp-symbolic-icons"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fa96ac6a1a85c0cb16dccab5c03ae1e651a3482cde4a93f792956977bc19108d"


def post_install(self):
    self.uninstall("usr/bin")
