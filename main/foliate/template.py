pkgname = "foliate"
pkgver = "3.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gjs-devel",
    "libadwaita-devel",
    "webkitgtk4-devel",
]
depends = [
    "gjs",
    "libadwaita",
    "webkitgtk4",
]
checkdepends = ["appstream-glib"]
pkgdesc = "GTK e-book reader"
license = "GPL-3.0-or-later"
url = "https://johnfactotum.github.io/foliate"
source = f"https://github.com/johnfactotum/foliate/releases/download/{pkgver}/com.github.johnfactotum.Foliate-{pkgver}.tar.xz"
sha256 = "09d0cc0a34426a2e57af25d67147dfe9b77ebf638a5a041b9f5c42499c4db672"
options = ["!cross"]
