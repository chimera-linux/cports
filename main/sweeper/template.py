pkgname = "sweeper"
pkgver = "24.12.2"
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
sha256 = "fbcbaaace8889857e9d76c01ad26dcbd649b6884ec26dbaedcd723775eff37e9"
