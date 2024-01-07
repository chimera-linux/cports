pkgname = "cairomm1.0"
pkgver = "1.14.5"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dboost-shared=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["cairo-devel", "libsigc++2-devel"]
checkdepends = ["boost-devel", "fontconfig-devel", "fonts-dejavu-otf"]
pkgdesc = "C++ bindings to Cairo graphics library (1.14)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://www.cairographics.org/cairomm"
source = f"https://cairographics.org/releases/cairomm-{pkgver}.tar.xz"
sha256 = "70136203540c884e89ce1c9edfb6369b9953937f6cd596d97c78c9758a5d48db"


@subpackage("cairomm1.0-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/cairomm-1.0",
        ]
    )
