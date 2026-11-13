pkgname = "syntax-highlighting"
pkgver = "6.32.0"
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
sha256 = "561d01001509299ad0578a02365e6bc714f2799724ac5980bc021c1ec2a44a67"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("syntax-highlighting-devel")
def _(self):
    return self.default_devel()
