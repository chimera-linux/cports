pkgname = "d-spy"
pkgver = "1.10.0"
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
source = f"{url}/-/archive/{pkgver}/d-spy-{pkgver}.tar.gz"
sha256 = "7e9a852a5f29572aee61b20f435f5b374902e22fe8c0a74ef29fb29850bf6090"
hardening = ["vis", "!cfi"]


@subpackage("d-spy-devel")
def _(self):
    return self.default_devel()
