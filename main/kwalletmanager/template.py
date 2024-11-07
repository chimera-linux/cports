pkgname = "kwalletmanager"
pkgver = "24.08.3"
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
sha256 = "aebd0c0d9327661774a137f1a575f4b895eff0085f3c83b21fb1008b7bb1a4bf"
hardening = ["vis"]
