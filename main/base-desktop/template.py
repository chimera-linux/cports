pkgname = "base-desktop"
pkgver = "0.1"
pkgrel = 3
build_style = "meta"
depends = ["base-full"]
pkgdesc = "Deprecated transitional package for Chimera desktops"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-desktop-gnome")
def _gnome(self):
    self.subdesc = "GNOME"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "gnome",
    ]
    return []
