pkgname = "ktextwidgets"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qttools-devel",
    "sonnet-devel",
]
pkgdesc = "KDE Text editing widgets"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktextwidgets-{pkgver}.tar.xz"
sha256 = "b122f86b179f9f9f7818a71dbcc3ce29ddac9605e55bf1d2fb885f3b8fe9c0b2"
hardening = ["vis"]


@subpackage("ktextwidgets-devel")
def _(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel()
