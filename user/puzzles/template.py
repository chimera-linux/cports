pkgname = "puzzles"
pkgver = "0_git20241108"
_gitrev = "8e83f39"
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
source = f"https://git.tartarus.org/?p=simon/puzzles.git;a=snapshot;h={_gitrev};sf=tgz>puzzles-{pkgver}.tar.gz"
sha256 = "9483442923e8a8f72214c2ddb80cfa62774e3f5d7827943c849b850ae5ca61f6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENCE")
