pkgname = "sweeper"
pkgver = "24.08.3"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/sweeper"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/sweeper-{pkgver}.tar.xz"
sha256 = "a5e9a77eb9986b3655e8b65914e6657db66032f20ed2f99d80d3c5423adb081f"
