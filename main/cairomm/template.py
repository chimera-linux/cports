pkgname = "cairomm"
pkgver = "1.19.1"
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
sha256 = "06881a0167d84962c74db318427c5be663d30b8ea5c60740a9dc36a9c1961b54"


@subpackage("cairomm-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/cairomm-1.16",
        ]
    )
