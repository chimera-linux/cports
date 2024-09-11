pkgname = "puzzles"
pkgver = "0_git20240911"
_gitrev = "cd97968"
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
sha256 = "d25a7c0c8be5083f029f350de85ba4c6b78c2401c4bf87ae3893c9d7c2a9c6b0"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENCE")
