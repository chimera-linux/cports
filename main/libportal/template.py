pkgname = "libportal"
pkgver = "0.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dbackends=gtk3"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala"
]
makedepends = ["libglib-devel", "gtk+3-devel"]
pkgdesc = "Flatpak portal library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://github.com/flatpak/libportal"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d8c8cb18a34e5eeb26a39c94044c955995b01de0e139caac5e18c076cf821b3b"

@subpackage("libportal-gtk3")
def _gtk3(self):
    self.pkgdesc = f"{pkgdesc} (Gtk+3 backend)"

    return ["usr/lib/girepository-1.0/XdpGtk3*", "usr/lib/libportal-gtk3.so.*"]

@subpackage("libportal-devel")
def _devel(self):
    return self.default_devel()
