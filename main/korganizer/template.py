pkgname = "korganizer"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "akonadi-sqlite-.*"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-contacts-devel",
    "akonadi-devel",
    "calendarsupport-devel",
    "eventviews-devel",
    "incidenceeditor-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kitemviews-devel",
    "kjobwidgets-devel",
    "kldap-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knewstuff-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "kuserfeedback-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libkdepim-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
depends = ["kdepim-runtime"]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE Kontact calendar scheduler"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://apps.kde.org/korganizer"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/korganizer-{pkgver}.tar.xz"
sha256 = "dd18b2c26bb1af4ccd4ee66a4a203c8c6ab59f639bc6f5a09a3b4c8d1bf55cee"
