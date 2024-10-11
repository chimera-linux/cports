pkgname = "kconfigwidgets"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcodecs-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Widgets for configuration dialogs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/kconfigwidgets"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kconfigwidgets-{pkgver}.tar.xz"
sha256 = "c079c67c578930baafae241bb4f252c63fdd125e44f1fb952e39bae3c9859cd1"
hardening = ["vis"]


@subpackage("kconfigwidgets-devel")
def _(self):
    self.depends += [
        "kcodecs-devel",
        "kconfig-devel",
        "kwidgetsaddons-devel",
        "kcolorscheme-devel",
    ]

    return self.default_devel()
