pkgname = "base-desktop"
pkgver = "0.1"
pkgrel = 3
build_style = "meta"
depends = ["base-full"]
pkgdesc = "Deprecated transitional package for Chimera desktops"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-desktop-gnome")
def _(self):
    self.subdesc = "GNOME"
    self.install_if = [self.parent]
    self.depends = [
        self.parent,
        "gnome",
    ]
    return []
