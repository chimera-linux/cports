pkgname = "kcoreaddons"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt6 addon library with a collection of non-GUI utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/kcoreaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcoreaddons-{pkgver}.tar.xz"
sha256 = "b8bb93bac2a1175ff60583f6fca14b8707eb878eefe074121741b3c85cc5c756"
# FIXME: cfi breaks at least kpluginfactorytest
hardening = ["vis", "!cfi"]


@subpackage("kcoreaddons-devel")
def _devel(self):
    return self.default_devel()
