pkgname = "keditbookmarks"
pkgver = "24.05.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://github.com/KDE/keditbookmarks"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/keditbookmarks-{pkgver}.tar.xz"
)
sha256 = "a3f2b24f9128f7804d92e59487276f63e8067af8b76e1b338274cd83df86c5e1"
