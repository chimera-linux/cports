pkgname = "cairomm"
pkgver = "1.16.2"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dboost-shared=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["cairo-devel", "libsigc++-devel"]
checkdepends = ["boost-devel", "fontconfig-devel", "fonts-dejavu-otf"]
pkgdesc = "C++ bindings to Cairo graphics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.cairographics.org/cairomm"
source = f"http://cairographics.org/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "6a63bf98a97dda2b0f55e34d1b5f3fb909ef8b70f9b8d382cb1ff3978e7dc13f"


@subpackage("cairomm-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/cairomm-1.16",
        ]
    )
