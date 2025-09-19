pkgname = "kpat"
pkgver = "25.08.1"
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
    "black-hole-solver-devel",
    "freecell-solver-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knewstuff-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkdegames-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
depends = ["libkdegames-carddecks"]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE solitaire collection"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kpat"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpat-{pkgver}.tar.xz"
sha256 = "09656293e06d82b8849aea9fe50b428f03fcc42e15c91bdc05a34ab18ed217fe"
