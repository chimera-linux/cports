pkgname = "kcompletion"
pkgver = "6.11.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Powerful completion framework"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcompletion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcompletion-{pkgver}.tar.xz"
sha256 = "c812b60de4530de3003916e45fbab121c5f9f576e2430ab2cdf0e3e4c9041852"
hardening = ["vis"]


@subpackage("kcompletion-devel")
def _(self):
    return self.default_devel()
