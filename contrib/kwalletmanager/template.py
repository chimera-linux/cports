pkgname = "kwalletmanager"
pkgver = "24.05.1"
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
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE KWallet GUI manager"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/utilities/kwalletmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kwalletmanager-{pkgver}.tar.xz"
)
sha256 = "1c297bf453b92cc569b785a0d8384fa662f485b163c529be1723798b91c139a8"
# CFI: check
hardening = ["vis", "!cfi"]
