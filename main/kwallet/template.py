pkgname = "kwallet"
pkgver = "6.28.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gpgmepp-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kservice-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libgcrypt-devel",
    "libsecret-devel",
    "qca-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Safe desktop-wide storage for passwords"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kwallet/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kwallet-{pkgver}.tar.xz"
sha256 = "e21130c86ffa0be49065648f4e753d63d3d786fab876f511d9d09da16480f691"
hardening = ["vis"]


@subpackage("kwallet-devel")
def _(self):
    return self.default_devel()
