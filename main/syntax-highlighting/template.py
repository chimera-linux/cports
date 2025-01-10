pkgname = "syntax-highlighting"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Syntax highlighting engine for structured text and code"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://api.kde.org/frameworks/syntax-highlighting/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syntax-highlighting-{pkgver}.tar.xz"
sha256 = "b5b5e343ff27bc5c95be0051d5606dfcb3295f835830e7fc6dac8d2863891699"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("syntax-highlighting-devel")
def _(self):
    return self.default_devel()
