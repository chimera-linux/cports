pkgname = "syntax-highlighting"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
license = "MIT"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syntax-highlighting-{pkgver}.tar.xz"
sha256 = "924c4cfab4043ede9a40bc55721a62515c7b83c6b84c0bdcc29cd3cdf89b09b4"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("syntax-highlighting-devel")
def _(self):
    return self.default_devel()
