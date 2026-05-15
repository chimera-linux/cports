pkgname = "gnome-shell-extension-appindicator"
pkgver = "64"
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
sha256 = "e8a9136a134dc52c76b75ae4b89e71cee6fbe2061dd318d0f818f088f8253411"
