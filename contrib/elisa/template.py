pkgname = "elisa"
pkgver = "24.05.2"
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
    "kconfigwidgets-devel",
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
checkdepends = ["xwayland-run"] + depends
pkgdesc = "KDE music player"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://apps.kde.org/elisa"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/elisa-{pkgver}.tar.xz"
sha256 = "c0177ef091800dc36815bfcc7f268addbd65d3bc5a1c5c385f124c42899d1b0e"
# CFI: crashes on start
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]
