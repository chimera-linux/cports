pkgname = "filelight"
pkgver = "24.08.2"
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
maintainer = "psykose <alice@ayaya.dev>"
license = " GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/filelight"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/filelight-{pkgver}.tar.xz"
sha256 = "5e904cdf4573fa5b8578e4157da348ad46e7281992bfbd6af59c9430e16ba94e"
hardening = ["vis"]
