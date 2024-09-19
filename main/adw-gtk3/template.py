pkgname = "adw-gtk3"
pkgver = "5.4"
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
source = f"https://github.com/lassekongo83/adw-gtk3/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1e3c7d6517c254ad7cc233274b1ded600db50f52c11f96d7000c098f9e9c0f9e"
