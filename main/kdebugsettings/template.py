pkgname = "kdebugsettings"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kwidgetsaddons-devel",
    "kcompletion-devel",
    "kxmlgui-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE QLoggingCategory display editor"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kdebugsettings"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdebugsettings-{pkgver}.tar.xz"
)
sha256 = "c63f443d617fb6f8f42a7b8edfd4f3c65a6f63e3cb94d4b701837c7cd1d714ce"
