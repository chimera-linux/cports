pkgname = "accessibility-inspector"
pkgver = "25.08.2"
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
sha256 = "67c458897f862be6a8434cc8e71e41cb9f7be15b474f4b7b6b44f00bafb65261"
