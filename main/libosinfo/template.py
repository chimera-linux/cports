pkgname = "libosinfo"
pkgver = "1.11.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-introspection=enabled",
    "-Denable-vala=enabled",
    "-Denable-gtk-doc=false",
]
make_check_env = {"MAKE": "gmake"}
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
    "perl",
    "gettext",
]
makedepends = [
    "libxslt-devel",
    "libxml2-devel",
    "glib-devel",
    "libsoup-devel",
]
depends = ["hwdata", "osinfo-db", "gmake"]
checkdepends = list(depends)
pkgdesc = "GObject API for managing information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://libosinfo.org"
source = f"https://gitlab.com/{pkgname}/{pkgname}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "927826e666f498cef106ef1bf22af4cc0cd56749f246ab15acdc1be05695a6eb"
options = ["!cross"]


@subpackage("libosinfo-devel")
def _devel(self):
    return self.default_devel()
