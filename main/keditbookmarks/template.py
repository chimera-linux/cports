pkgname = "keditbookmarks"
pkgver = "25.12.1"
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
    "kbookmarks-devel",
    "kcodecs-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libx11-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE bookmarks editor"
license = "GPL-2.0-only"
url = "https://invent.kde.org/utilities/keditbookmarks"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/keditbookmarks-{pkgver}.tar.xz"
)
sha256 = "b2b2d233aff98cb79bef89511e2e2688ff0711a8f5ec03ca97f5449fc9bd3bbc"
