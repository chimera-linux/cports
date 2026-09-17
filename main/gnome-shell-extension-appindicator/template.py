pkgname = "gnome-shell-extension-appindicator"
pkgver = "65"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "jq",
    "meson",
]
depends = ["gnome-shell"]
pkgdesc = "AppIndicator/KStatusNotifierItem support for GNOME"
license = "GPL-2.0-or-later"
url = "https://github.com/ubuntu/gnome-shell-extension-appindicator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a55eb3ffc8882f7d1f974fbdce2c2f72c1e14b1bf9ba72af2a99622be022287f"
