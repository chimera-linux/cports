pkgname = "filelight"
pkgver = "24.05.0"
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
sha256 = "0c776ff0db323d47dfb96772cef63b2311eceede940494943b0f3e8bf8a9ab8c"
# CFI: check
hardening = ["vis", "!cfi"]
