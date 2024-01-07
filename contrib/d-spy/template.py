pkgname = "d-spy"
pkgver = "1.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext-devel",
    "glib-devel",
    "gtk-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "D-Bus inspector and debugger"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/d-spy"
source = f"https://gitlab.gnome.org/GNOME/d-spy/-/archive/{pkgver}/d-spy-{pkgver}.tar.gz"
sha256 = "bb11d69662415ed61e9d4c2da03a6d6b4bf2877e46f09ec8f4fa3837c7977245"
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("d-spy-devel")
def _devel(self):
    return self.default_devel()
