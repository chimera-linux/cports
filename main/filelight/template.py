pkgname = "filelight"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
# can segfault in parallel
make_check_args = ["-j1"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE disk usage visualizer"
license = " GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/filelight"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/filelight-{pkgver}.tar.xz"
sha256 = "ec3a4345bb98cfc0bbe5f1faf9c021f3552155ee33f2e82623ae623746b187e9"
hardening = ["vis"]
