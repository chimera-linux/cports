pkgname = "ktextwidgets"
pkgver = "6.9.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/ktextwidgets/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktextwidgets-{pkgver}.tar.xz"
sha256 = "da966c6e01cfb3125ec31a4d2149372a19d1481441869ece9fcef3b70bb3514d"
hardening = ["vis"]


@subpackage("ktextwidgets-devel")
def _(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel()
