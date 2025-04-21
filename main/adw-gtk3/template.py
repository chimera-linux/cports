pkgname = "adw-gtk3"
pkgver = "5.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "sassc",
]
pkgdesc = "Libadwaita's theme for gtk3"
license = "LGPL-2.1-or-later"
url = "https://github.com/lassekongo83/adw-gtk3"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1439d432248a661ccc513a90ae1e5e9e65cac69842cbc090f09ec4f994c8b749"
