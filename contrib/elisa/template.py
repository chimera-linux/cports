pkgname = "elisa"
pkgver = "24.08.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://apps.kde.org/elisa"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/elisa-{pkgver}.tar.xz"
sha256 = "7f1ceb99a4ae57a1b609fee4f4903b0243f3cc84a854e1d41cd222a42085ee81"
hardening = ["vis"]
# TODO
options = ["!cross"]
