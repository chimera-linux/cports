pkgname = "puzzles"
pkgver = "0_git20240909"
_gitrev = "53ceb98"
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
sha256 = "8c03972b1c15ce99538b3062c2d8ee455f47075264275e78cf97678cc3a880b6"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENCE")
