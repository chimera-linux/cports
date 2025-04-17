pkgname = "sweeper"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kbookmarks-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "ktextwidgets-devel",
    "kxmlgui-devel",
    "plasma-activities-stats-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE cache cleaner"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/sweeper"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/sweeper-{pkgver}.tar.xz"
sha256 = "70b8fd018430e025f214161c05785d2665cda48499e3bab477a25cdbcde7f06c"
