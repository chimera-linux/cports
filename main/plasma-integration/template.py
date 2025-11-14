pkgname = "plasma-integration"
pkgver = "6.5.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
make_check_args = [
    "-E",
    "(kdeplatformtheme|"  # 5/9 failing subtests due to differing values, kdeplatformtheme_unittest.cpp:(127,167,221,230,295)
    "kfontsettingsdata|"  # testFontsChanged() 'm_appChangedFont' returned FALSE, kfontsettingsdata_unittest.cpp:93
    "kfiledialog_unittest6|"  # SEGFAULT after 9s in testGetSaveFileUrl(), kfiledialog_unittest.cpp:144
    "kfiledialogqml)",  # testShowDialog* can't find KIO KFileWidget, kfiledialogqml_unittest.cpp:38
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kxmlgui-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qgenericunixthemes_p.h/qgenericunixservices_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
]
checkdepends = [
    "breeze",
    "dbus",
]
pkgdesc = "Qt Platform Theme integration plugins for the Plasma workspaces"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-integration"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-integration-{pkgver}.tar.xz"
sha256 = "8a13fcfd5a61cf9ff683754fe7013e24f2285b8f39f6799ba1df7bc9ee5f7ee4"
hardening = ["vis"]
