pkgname = "kconfigwidgets"
pkgver = "6.20.0"
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
    "qt6-qtbase-private-devel",  # qguiapplication_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Widgets for configuration dialogs"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/kconfigwidgets"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kconfigwidgets-{pkgver}.tar.xz"
sha256 = "5c5e8dc7e986d85c3602b8a52b8d8909f91e7433ecad8037099491250f5f4e36"
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
