pkgname = "slop"
pkgver = "7.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glew-devel",
    "glm",
    "icu-devel",
    "libxext-devel",
    "libxrender-devel",
]
pkgdesc = "Select region of X11 display"
maintainer = "peri <peri@periwinkle.sh>"
license = "GPL-3.0-or-later"
url = "https://github.com/naelstrof/slop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ec45f9a69d7a24df621f5c634d202451ddca987d550cf588c5c427b99106fb6b"


@subpackage("slop-devel")
def _(self):
    return self.default_devel()
