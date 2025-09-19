pkgname = "accessibility-inspector"
pkgver = "25.08.1"
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
sha256 = "bb1adda15a2798adc1a48682a6b723dd5f6911c9e165ab7fa9952bee84ea3e71"
