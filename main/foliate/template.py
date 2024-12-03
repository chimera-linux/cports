pkgname = "foliate"
pkgver = "3.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gtk-update-icon-cache",
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://johnfactotum.github.io/foliate"
source = f"https://github.com/johnfactotum/foliate/releases/download/{pkgver}/com.github.johnfactotum.Foliate-{pkgver}.tar.xz"
sha256 = "714d42d54e103f4a3c367bf18186a56401228b7ee1175224e760ae59f204e1e6"
options = ["!cross"]
