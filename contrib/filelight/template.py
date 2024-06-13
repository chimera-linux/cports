pkgname = "filelight"
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
sha256 = "c5d6b8fb946c096f5cd806988aaea134b6c0c211f0de478217da5c7b237cec0b"
# CFI: check
hardening = ["vis", "!cfi"]
