pkgname = "slop"
pkgver = "7.7"
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
license = "GPL-3.0-or-later"
url = "https://github.com/naelstrof/slop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a69a6e5c41d7fff1c6aa35b367a5c5a6dc98e621fa9a1908808d6308c2b40f4e"


@subpackage("slop-devel")
def _(self):
    return self.default_devel()
