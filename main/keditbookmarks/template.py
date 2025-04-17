pkgname = "keditbookmarks"
pkgver = "25.04.0"
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
url = "https://github.com/KDE/keditbookmarks"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/keditbookmarks-{pkgver}.tar.xz"
)
sha256 = "007ba23e521a92cb1ce952698db0ae2c583a94d428ed0fea4af49e60a48a33dd"
