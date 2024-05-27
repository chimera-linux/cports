pkgname = "foliate"
pkgver = "3.1.1"
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
sha256 = "1bda9cd32b4d9a2480b0fc4f9884ad04450bd96fdb30a48ab9c1e7b6ec625144"
options = ["!cross"]
