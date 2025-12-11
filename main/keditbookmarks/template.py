pkgname = "keditbookmarks"
pkgver = "25.12.0"
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
sha256 = "ebbe1598cc6dbd78a72d63566fd8e4b0849bf4b5e3bcb4bb7b8b578f17b0a247"
