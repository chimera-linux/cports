pkgname = "libmanette"
pkgver = "0.2.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgudev=enabled"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "libevdev-devel", "libgudev-devel"]
pkgdesc = "Simple GObject game controller library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libmanette"
source = f"$(GNOME_SITE)/libmanette/{pkgver[:-2]}/libmanette-{pkgver}.tar.xz"
sha256 = "29366be5452f60a74c65fc64ffe2d74eddd4e6e6824c2cefa567a43bd92b688f"


@subpackage("libmanette-devel")
def _(self):
    return self.default_devel()
