pkgname = "xapp-symbolic-icons"
pkgver = "1.0.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Set of symbolic icons for Gtk applications and projects"
license = "LGPL-3.0-or-later"
url = "https://github.com/xapp-project/xapp-symbolic-icons"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0ebb603eaa34f34d44bc419119595c91785caf0e29a2ad2adaa7fea9cc2e6ebb"


@subpackage("xapp-symbolic-icons-progs")
def _(self):
    self.depends = [self.parent, "python"]

    return ["usr/bin"]
