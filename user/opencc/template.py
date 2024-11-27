pkgname = "opencc"
pkgver = "1.1.9"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["pkgconf", "cmake", "ninja", "python"]
pkgdesc = "Open Chinese conversion library"
maintainer = "metalparade <comer@live.cn>"
license = "Apache-2.0"
url = "https://github.com/BYVoid/OpenCC"
source = f"{url}/archive/refs/tags/ver.{pkgver}.tar.gz"
sha256 = "ad4bcd8d87219a240a236d4a55c9decd2132a9436697d2882ead85c8939b0a99"


@subpackage("opencc-devel")
def _(self):
    return self.default_devel()
