pkgname = "elisa"
pkgver = "26.08.2"
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
sha256 = "432331a84ade68fd519974c91ebd789bf5670b9be24e9acc8b5def3140b30b1c"
hardening = ["vis"]
# TODO
options = ["!cross"]
