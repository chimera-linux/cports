pkgname = "foliate"
pkgver = "3.2.1"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://johnfactotum.github.io/foliate"
source = f"https://github.com/johnfactotum/foliate/releases/download/{pkgver}/com.github.johnfactotum.Foliate-{pkgver}.tar.xz"
sha256 = "01c27a8c481a9ebc4a3237e2947c3e86ef36cc0fac2f4199e7a79e554d676ea4"
options = ["!cross"]
