pkgname = "sweeper"
pkgver = "25.12.1"
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
sha256 = "04f28a573610ca910012586ce991a490efbbcb2abeda2c10473404ed60b77dae"
