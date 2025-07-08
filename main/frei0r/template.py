pkgname = "frei0r"
pkgver = "2.3.3"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "gavl-devel",
    "opencv-devel",
]
pkgdesc = "Collection of video plugins"
license = "GPL-2.0-or-later"
url = "https://frei0r.dyne.org"
source = f"https://github.com/dyne/frei0r/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aeeefe3a9b44761b2cf110017d2b1dfa2ceeb873da96d283ba5157380c5d0ce5"


@subpackage("frei0r-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
