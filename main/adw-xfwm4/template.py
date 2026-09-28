pkgname = "adw-xfwm4"
pkgver = "0_git20230124"
_gitrev = "b0b163bac7d74e5c2d69451d9b1315389bb3c361"
pkgrel = 1
pkgdesc = "Libadwaita theme for xfwm4"
license = "LGPL-2.1-or-later"
url = "https://github.com/FabianOvrWrt/adw-xfwm4"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "8d51102bbfa6a7e7784c760629b85196626621573fa6642a7b985c96728b0f55"


def install(self):
    self.install_files("themes", "usr/share")

    # No idea why these are there
    self.uninstall("**/themerc~", glob=True)
