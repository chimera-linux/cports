pkgname = "adw-gtk3"
pkgver = "5.3"
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
sha256 = "73382b28c7bc1b44ebda4ed7f8f743d8ccd9deb5d429cbd04119753aefe1d392"
