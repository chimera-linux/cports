pkgname = "kbookmarks"
pkgver = "6.10.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kbookmarks/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kbookmarks-{pkgver}.tar.xz"
sha256 = "891eb12d2b9a2c3cdfbfdba250599c544d7186ce8d1ef07f4fc4cce1d57a945b"
hardening = ["vis"]


@subpackage("kbookmarks-devel")
def _(self):
    self.depends += ["kwidgetsaddons-devel"]

    return self.default_devel()
