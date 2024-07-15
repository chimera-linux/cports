pkgname = "ktextwidgets"
pkgver = "6.4.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ktextwidgets-{pkgver}.tar.xz"
sha256 = "08bc69461ade9944d35e5055f7bddd5313774d7a6c6727f12a68e58d1d3fce70"
hardening = ["vis"]


@subpackage("ktextwidgets-devel")
def _devel(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
