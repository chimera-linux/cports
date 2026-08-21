pkgname = "accessibility-inspector"
pkgver = "26.08.0"
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
sha256 = "8ac7d89aa00ee86855d9a84b7546693dc945b9acbe8942f9081090f4c89b5f61"
