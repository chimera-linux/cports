pkgname = "elisa"
pkgver = "26.04.3"
pkgrel = 0
build_style = "cmake"
# flaky
make_check_args = ["-E", "(localfilelistingtest)"]
make_check_wrapper = [
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kxmlgui-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    # "vlc-devel",
]
depends = ["kirigami-addons"]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE music player"
license = "LGPL-3.0-or-later"
url = "https://apps.kde.org/elisa"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/elisa-{pkgver}.tar.xz"
sha256 = "361e4f5bfe373f340e18e80fe35b8d7c1b6c8f65970b867a2e27e81103ce25d5"
hardening = ["vis"]
# TODO
options = ["!cross"]
