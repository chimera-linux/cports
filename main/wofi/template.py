pkgname = "wofi"
pkgver = "1.5.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["gtk+3-devel", "wayland-devel"]
pkgdesc = "Launcher/menu program for wlroots-based wayland compositors"
license = "GPL-3.0-or-later"
url = "https://sr.ht/~scoopta/wofi"
source = f"https://hg.sr.ht/~scoopta/wofi/archive/v{pkgver}.tar.gz"
sha256 = "6216dc14d93cdb6170f89c1ca3aaacdeaa44862fbc9be947d614be266a9c49f6"
# vis breaks all modes
hardening = ["!vis"]
# no check
options = ["!check"]


@subpackage("wofi-devel")
def _(self):
    return self.default_devel()
