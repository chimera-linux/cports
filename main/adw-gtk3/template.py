pkgname = "adw-gtk3"
pkgver = "5.8"
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
sha256 = "4dec5265f250473082dcba38995f44024b9d87a1e91c5adf79b9fdabf0c59fd4"
