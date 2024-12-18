pkgname = "accessibility-inspector"
pkgver = "24.12.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://apps.kde.org/accessibilityinspector"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/accessibility-inspector-{pkgver}.tar.xz"
sha256 = "fe2d6ed9c4d149329c48c3283f3c3f5088fcc876ad05d366ca80e4dd7ef2674c"
