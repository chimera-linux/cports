pkgname = "constrict"
pkgver = "26.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "Compress videos to target sizes"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Constrict"
source = f"https://gitlab.gnome.org/World/Constrict/-/archive/{pkgver}/Constrict-{pkgver}.tar.gz"
sha256 = "a84bc809519bec7d6e302861c4e508fb97305cb44a96d8e924f0b4907a794d39"
