pkgname = "wofi"
pkgver = "1.4.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtk+3-devel", "wayland-devel"]
pkgdesc = "Launcher/menu program for wlroots-based wayland compositors"
maintainer = "avgwst <avgwst@tutanota.de>"
license = "GPL-3.0-or-later"
url = "https://sr.ht/~scoopta/wofi"
source = f"https://hg.sr.ht/~scoopta/wofi/archive/v{pkgver}.tar.gz"
sha256 = "e95e35c03551c39178c16ad6213a88e3883a236e942d7f2666c780d934c270bb"
# vis breaks all modes
hardening = ["!vis"]
# no check
options = ["!check"]


@subpackage("wofi-devel")
def _(self):
    return self.default_devel()
