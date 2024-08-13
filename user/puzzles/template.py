pkgname = "puzzles"
pkgver = "20240802"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DNAME_PREFIX=puzzles-"]
hostmakedepends = [
    "cmake",
    "fonts-dejavu",
    "halibut",
    "imagemagick",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
depends = ["cmd:xdg-open!xdg-utils"]
pkgdesc = "Collection of small programs which implement one-player puzzle games"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "MIT"
url = "https://www.chiark.greenend.org.uk/~sgtatham/puzzles"
source = f"{url}/puzzles-{pkgver}.1c1899e.tar.gz"
sha256 = "f72e9ea630011ba0acdf59b74fff24f0e4f33ae6271ff8312c5122b517d1c249"
hardening = ["vis", "cfi"]
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENCE")
