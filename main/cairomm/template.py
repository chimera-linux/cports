pkgname = "cairomm"
pkgver = "1.16.1"
pkgrel = 0
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
sha256 = "6f6060d8e98dd4b8acfee2295fddbdd38cf487c07c26aad8d1a83bb9bff4a2c6"

@subpackage("cairomm-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/cairomm-1.16",
    ])
