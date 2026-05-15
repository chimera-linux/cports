pkgname = "adw-gtk3"
pkgver = "6.5"
pkgrel = 0
pkgdesc = "Libadwaita's theme for gtk3"
license = "LGPL-2.1-or-later"
url = "https://github.com/lassekongo83/adw-gtk3"
source = f"{url}/releases/download/v{pkgver}/adw-gtk3v{pkgver}.tar.xz"
sha256 = "a81780fadfc432be0fc3d89c4ebb41aa28e4f032d42c36f9789c57dd10cfa41c"


def install(self):
    self.install_files("adw-gtk3", "usr/share/themes")
    self.install_files("adw-gtk3-dark", "usr/share/themes")
