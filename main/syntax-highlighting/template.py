pkgname = "syntax-highlighting"
pkgver = "6.15.0"
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
license = "MIT"
url = "https://api.kde.org/frameworks/syntax-highlighting/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/syntax-highlighting-{pkgver}.tar.xz"
sha256 = "7b2490e6ba656fd85974d9776aede828a0a450eb44ead7969d484ed9486c74cc"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("syntax-highlighting-devel")
def _(self):
    return self.default_devel()
