pkgname = "filelight"
pkgver = "24.12.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = " GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/filelight"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/filelight-{pkgver}.tar.xz"
sha256 = "f8102f0d74f7dc3b6f17906993cbc63570f498c6f016a39a13503fdbe6d3b6b0"
hardening = ["vis"]
