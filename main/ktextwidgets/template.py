pkgname = "ktextwidgets"
pkgver = "6.27.0"
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
sha256 = "03c35d8899559efc17b4f74e86eefd8358dafd7aa9311c89b9c09f7b35700756"
hardening = ["vis"]


@subpackage("ktextwidgets-devel")
def _(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel()
