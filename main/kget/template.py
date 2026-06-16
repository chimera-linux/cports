pkgname = "kget"
pkgver = "26.04.2"
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
    "qgpgme-devel",
    "qt6-qtbase-devel",
    "sqlite-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE download manager"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kget"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kget-{pkgver}.tar.xz"
sha256 = "e4643214ddc3c43eada345eeb33418963c9f880903a0410db2320423521be669"
