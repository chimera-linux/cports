pkgname = "filelight"
pkgver = "24.05.2"
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
    "kirigami-devel",
    "kirigami-addons-devel",
    "kdoctools-devel",
    "qqc2-desktop-style-devel",
    "kcoreaddons-devel",
    "kio-devel",
    "kxmlgui-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE disk usage visualizer"
maintainer = "psykose <alice@ayaya.dev>"
license = " GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/filelight"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/filelight-{pkgver}.tar.xz"
sha256 = "33d3b61f7d9332f2506b58b3fa5ac0b2a0308e2f2e21be818e8b9da5207e2b56"
# CFI: check
hardening = ["vis", "!cfi"]
