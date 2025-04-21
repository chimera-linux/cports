pkgname = "cairomm"
pkgver = "1.18.0"
pkgrel = 5
build_style = "meson"
configure_args = ["-Dboost-shared=true"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["cairo-devel", "libsigc++-devel"]
checkdepends = ["boost-devel", "fontconfig-devel", "fonts-dejavu-otf"]
pkgdesc = "C++ bindings to Cairo graphics library"
license = "LGPL-2.1-or-later"
url = "https://www.cairographics.org/cairomm"
source = f"https://cairographics.org/releases/cairomm-{pkgver}.tar.xz"
sha256 = "b81255394e3ea8e8aa887276d22afa8985fc8daef60692eb2407d23049f03cfb"


@subpackage("cairomm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/cairomm-1.16",
        ]
    )
