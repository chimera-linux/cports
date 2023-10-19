pkgname = "adw-gtk3"
pkgver = "5.1"
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
sha256 = "c71acf08341e9568b2503eda51a64a8c6489af53f256f18da8b1e917cb14c0d3"
