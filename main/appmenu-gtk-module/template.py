pkgname = "appmenu-gtk-module"
pkgver = "25.04"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk=3"]
meson_dir = "subprojects/appmenu-gtk-module"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "GTK module for appmenu"
license = "LGPL-3.0-only"
url = "https://gitlab.com/vala-panel-project/vala-panel-appmenu"
source = f"{url}/-/archive/{pkgver}/vala-panel-appmenu-{pkgver}.tar.gz"
sha256 = "48d0be87b260056a65a9056a9be7e190b67a508540ebcb1fc18a67349cca0177"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("appmenu-gtk-module-devel")
def _(self):
    return self.default_devel()
