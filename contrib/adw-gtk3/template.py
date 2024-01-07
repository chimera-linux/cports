pkgname = "adw-gtk3"
pkgver = "5.2"
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
sha256 = "1265b9dbc933bf602da1c419e515752bc8d7b9e6f8a09eafd740315d321501d7"
