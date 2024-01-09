pkgname = "d-spy"
pkgver = "1.9.0"
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
sha256 = "89b3b5aec27b88c8d99ebc9c79ecb9b7af0789dd39f487a1c25c70293b394209"
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("d-spy-devel")
def _devel(self):
    return self.default_devel()
