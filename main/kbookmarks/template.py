pkgname = "kbookmarks"
pkgver = "6.9.0"
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
sha256 = "932234bedbf5a5887f23c610010c8c70b36b5dce4f4c4c5d76f47a92ce8e577a"
hardening = ["vis"]


@subpackage("kbookmarks-devel")
def _(self):
    self.depends += ["kwidgetsaddons-devel"]

    return self.default_devel()
