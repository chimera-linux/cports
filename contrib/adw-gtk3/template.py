pkgname = "adw-gtk3"
pkgver = "4.9"
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
sha256 = "4ca2082cb5c7fe6ece1a060b9d1952fbae338529ccbcb9fe40bc554bd0a04048"
