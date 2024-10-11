pkgname = "adw-gtk3"
pkgver = "5.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "sassc",
]
pkgdesc = "Libadwaita's theme for gtk3"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lassekongo83/adw-gtk3"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "02433c9ef67267776e0a4c822e28b6810063a68c1ecf2f17f0936a9c45a20b9b"
