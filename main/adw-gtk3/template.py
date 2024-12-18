pkgname = "adw-gtk3"
pkgver = "5.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "sassc",
]
pkgdesc = "Libadwaita's theme for gtk3"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lassekongo83/adw-gtk3"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e947de328a87678ae76f41061d94931523ee6015cb83bba8af7a5cd6375265b2"
