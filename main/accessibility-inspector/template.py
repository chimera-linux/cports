pkgname = "accessibility-inspector"
pkgver = "25.12.1"
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
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kxmlgui-devel",
    "libqaccessibilityclient-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE application accessibility tree inspector"
license = "LGPL-2.0-or-later"
url = "https://apps.kde.org/accessibilityinspector"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/accessibility-inspector-{pkgver}.tar.xz"
sha256 = "1a24a4aea39f95456811f8292adb45df822ea9b07b7da5e95f342dcb30776775"
