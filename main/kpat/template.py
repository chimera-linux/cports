pkgname = "kpat"
pkgver = "24.08.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kpat"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpat-{pkgver}.tar.xz"
sha256 = "2d9da86315e424b484040e191143be0a936ea438543d078d96e77dc5283a04f2"
