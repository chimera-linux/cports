pkgname = "puzzles"
pkgver = "0_git20251021"
_gitrev = "790f585"
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
license = "MIT"
url = "https://www.chiark.greenend.org.uk/~sgtatham/puzzles"
source = f"https://git.tartarus.org/?p=simon/puzzles.git;a=snapshot;h={_gitrev};sf=tgz>puzzles-{pkgver}.tar.gz"
sha256 = "a22bf8a61122661a081ded70cc5970f36d3dcc8d4ec443acf53d2e9d56df7496"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENCE")
