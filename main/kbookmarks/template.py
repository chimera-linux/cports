pkgname = "kbookmarks"
pkgver = "6.26.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Bookmarks management library"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kbookmarks/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kbookmarks-{pkgver}.tar.xz"
sha256 = "82e8794281870686da9e7e7b5ddc0839f50b15d919357490d508faccb2635030"
hardening = ["vis"]


@subpackage("kbookmarks-devel")
def _(self):
    self.depends += ["kwidgetsaddons-devel"]

    return self.default_devel()
