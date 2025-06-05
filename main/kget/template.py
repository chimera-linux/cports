pkgname = "kget"
pkgver = "25.04.2"
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
sha256 = "c6c9d107bdffbc2d19855f298c5634a341a82d6ca3e1b430ce608c7c10d580c1"
