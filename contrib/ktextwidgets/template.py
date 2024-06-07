pkgname = "ktextwidgets"
pkgver = "6.3.0"
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
sha256 = "9e9fb5aee6ba557ff53c5bf726cb8551efc4208038fda47ee5e9c44fd7d4385e"
hardening = ["vis", "!cfi"]


@subpackage("ktextwidgets-devel")
def _devel(self):
    self.depends += ["sonnet-devel", "ki18n-devel"]

    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
