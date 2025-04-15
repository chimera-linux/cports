pkgname = "ktextwidgets"
pkgver = "6.13.0"
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
url = "https://api.kde.org/frameworks/ktextwidgets/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktextwidgets-{pkgver}.tar.xz"
sha256 = "1ff29bf02b247f09ffaaafe4578f0977b51c42b67eef84fddb5677dd7d1edf2e"
hardening = ["vis"]


@subpackage("ktextwidgets-devel")
def _(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel()
