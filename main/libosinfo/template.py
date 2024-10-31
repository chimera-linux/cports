pkgname = "libosinfo"
pkgver = "1.12.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-introspection=enabled",
    "-Denable-vala=enabled",
    "-Denable-gtk-doc=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "perl",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "libsoup-devel",
    "libxml2-devel",
    "libxslt-devel",
]
depends = ["hwdata", "osinfo-db"]
checkdepends = [*depends]
pkgdesc = "GObject API for managing information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://libosinfo.org"
source = f"https://gitlab.com/libosinfo/libosinfo/-/archive/v{pkgver}/libosinfo-v{pkgver}.tar.gz"
sha256 = "3c52fb542d65d1ec5a10f87126d7513c2bd115eaa2f87fb91b15ba588708fc7b"
options = ["!cross"]


@subpackage("libosinfo-devel")
def _(self):
    return self.default_devel()
