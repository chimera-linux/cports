# update main/libportal too
pkgname = "libportal-qt6"
pkgver = "0.8.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dbackend-gtk3=disabled",
    "-Dbackend-gtk4=disabled",
    "-Dbackend-qt6=enabled",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "libportal-devel",
    "qt6-qtbase-devel",
]
origin = "libportal"
pkgdesc = "Flatpak portal library"
subdesc = "Qt6 backend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://github.com/flatpak/libportal"
source = f"{url}/releases/download/{pkgver}/libportal-{pkgver}.tar.xz"
sha256 = "281e54e4f8561125a65d20658f1462ab932b2b1258c376fed2137718441825ac"


def post_install(self):
    self.uninstall("usr/include/libportal")
    self.uninstall("usr/lib/girepository-1.0")
    self.uninstall("usr/lib/libportal.*", glob=True)
    self.uninstall("usr/lib/pkgconfig/libportal.pc")
    self.uninstall("usr/share")


@subpackage("libportal-qt6-devel")
def _(self):
    self.depends += ["libportal-devel"]
    return self.default_devel()
