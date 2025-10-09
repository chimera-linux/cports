pkgname = "kget"
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
    "boost-devel",
    "gpgme-qt-devel",
    "kcmutils-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemviews-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kstatusnotifieritem-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libktorrent-devel",
    "libmms-devel",
    "qt6-qtbase-devel",
    "sqlite-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE download manager"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kget"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kget-{pkgver}.tar.xz"
sha256 = "6214d5801acea5a7a7f1e87c268c617637213297bd3aa81708a6e97c3b37721f"
