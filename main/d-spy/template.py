pkgname = "d-spy"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext-devel",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "D-Bus inspector and debugger"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/d-spy"
source = f"{url}/-/archive/{pkgver}/d-spy-{pkgver}.tar.gz"
sha256 = "a757ecd21a2f53148e668c422065f6fdc7c15d431d20e059bf06c476756f306b"
hardening = ["vis", "!cfi"]


@subpackage("d-spy-devel")
def _(self):
    return self.default_devel()
