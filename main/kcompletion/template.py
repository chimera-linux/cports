pkgname = "kcompletion"
pkgver = "6.6.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcompletion-{pkgver}.tar.xz"
sha256 = "b80659b31fad437d19ec9486405d49f8db0cea709629e3b4ff0eb292ccf10b43"
hardening = ["vis"]


@subpackage("kcompletion-devel")
def _(self):
    return self.default_devel()
