pkgname = "puzzles"
pkgver = "0_git20250303"
_gitrev = "7da4641"
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
sha256 = "3d6ca23d6e03049a147c77dcf6a461d16359155e276f713e994ef6d658d3d1f1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENCE")
