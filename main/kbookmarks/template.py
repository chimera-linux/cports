pkgname = "kbookmarks"
pkgver = "6.22.0"
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
sha256 = "a90236ca53de4685af28b6c8643d81b2c0900faf83784bd2da3b52a1fd601a79"
hardening = ["vis"]


@subpackage("kbookmarks-devel")
def _(self):
    self.depends += ["kwidgetsaddons-devel"]

    return self.default_devel()
