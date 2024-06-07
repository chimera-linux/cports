pkgname = "knewstuff"
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
    "attica-devel",
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kpackage-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "syndication-devel",
]
pkgdesc = (
    "KDE Framework for downloading and sharing additional application data"
)
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/knewstuff/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/knewstuff-{pkgver}.tar.xz"
sha256 = "a16d16b22e94cb5159a3b1a071c5785729e3052baf9e33f2ab020b9032d967d7"
# FIXME: cfi causes crash when pressing "Get New Plugins..." button in the
# "Wallpaper" section of Plasma's system settings app
hardening = ["vis", "!cfi"]


@subpackage("knewstuff-devel")
def _devel(self):
    self.depends += [
        "attica-devel",
        "kcoreaddons-devel",
        "qt6-qtbase-devel",
    ]

    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
