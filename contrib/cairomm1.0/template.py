pkgname = "cairomm1.0"
pkgver = "1.14.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dboost-shared=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["cairo-devel", "libsigc++2-devel"]
checkdepends = ["boost-devel", "fontconfig-devel", "fonts-dejavu-otf"]
pkgdesc = "C++ bindings to Cairo graphics library (1.14)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://www.cairographics.org/cairomm"
source = f"http://cairographics.org/releases/cairomm-{pkgver}.tar.xz"
sha256 = "4749d25a2b2ef67cc0c014caaf5c87fa46792fc4b3ede186fb0fc932d2055158"

@subpackage("cairomm1.0-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/cairomm-1.0",
    ])
