# update main/libportal too
pkgname = "libportal-qt6"
pkgver = "0.8.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dbackend-gtk3=disabled",
    "-Dbackend-gtk4=disabled",
    "-Dbackend-qt6=enabled",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
sha256 = "ca38cd186e98388e4e92859506c9ecbd01db650ef871838b357b117d147f1541"


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
