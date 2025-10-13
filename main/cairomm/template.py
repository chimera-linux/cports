pkgname = "cairomm"
pkgver = "1.19.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dboost-shared=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["cairo-devel", "libsigc++-devel"]
checkdepends = ["boost-devel", "fontconfig-devel", "fonts-dejavu-otf"]
pkgdesc = "C++ bindings to Cairo graphics library"
license = "LGPL-2.1-or-later"
url = "https://www.cairographics.org/cairomm"
source = f"https://cairographics.org/releases/cairomm-{pkgver}.tar.xz"
sha256 = "8b14f03a0e5178c7ff8f7b288cb342a61711c84c9fbed6e663442cfcc873ce5b"


@subpackage("cairomm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/cairomm-1.16",
        ]
    )
