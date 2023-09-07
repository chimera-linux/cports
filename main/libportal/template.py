pkgname = "libportal"
pkgver = "0.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dbackend-gtk3=enabled",
    "-Dbackend-gtk4=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
]
makedepends = ["glib-devel", "gtk+3-devel", "gtk4-devel"]
pkgdesc = "Flatpak portal library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://github.com/flatpak/libportal"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "64635f03c9501b829d3b4fd2246e8d840f92e2ed14053e082ed3dddda7d725fb"


@subpackage("libportal-gtk3")
def _gtk3(self):
    self.pkgdesc = f"{pkgdesc} (Gtk+3 backend)"

    return ["usr/lib/girepository-1.0/XdpGtk3*", "usr/lib/libportal-gtk3.so.*"]


@subpackage("libportal-gtk4")
def _gtk4(self):
    self.pkgdesc = f"{pkgdesc} (Gtk4 backend)"

    return ["usr/lib/girepository-1.0/XdpGtk4*", "usr/lib/libportal-gtk4.so.*"]


@subpackage("libportal-devel")
def _devel(self):
    return self.default_devel()
