pkgname = "appmenu-gtk-module"
pkgver = "24.05"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://gitlab.com/vala-panel-project/vala-panel-appmenu"
source = f"{url}/-/archive/{pkgver}/vala-panel-appmenu-{pkgver}.tar.gz"
sha256 = "989f1e44cd38aad137640c1d39803e81bb37c971e18b6282abe4f3e0ba622703"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("appmenu-gtk-module-devel")
def _(self):
    return self.default_devel()
