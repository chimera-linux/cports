pkgname = "wofi"
pkgver = "1.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtk+3-devel", "wayland-devel"]
pkgdesc = "Launcher/menu program for wlroots-based wayland compositors"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later"
url = "https://sr.ht/~scoopta/wofi"
source = f"https://hg.sr.ht/~scoopta/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "7644e4e995bc027b7f3f411ceda82b3e2a72a4a424f6193663c27bbf00f23067"
# vis breaks all modes
hardening = ["!vis"]
# no check
options = ["!check"]


@subpackage("wofi-devel")
def _devel(self):
    return self.default_devel()
