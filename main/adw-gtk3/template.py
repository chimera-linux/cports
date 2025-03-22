pkgname = "adw-gtk3"
pkgver = "5.7"
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
sha256 = "b120582ba81d278d8a20dc1e85f29fc50927711efa40941394615f7deec3115c"
