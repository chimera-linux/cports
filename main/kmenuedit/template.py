pkgname = "kmenuedit"
pkgver = "6.7.5"
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
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemviews-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "sonnet-devel",
]
pkgdesc = "KDE menu editor"
license = "GPL-2.0-only"
url = "https://invent.kde.org/plasma/kmenuedit"
source = f"$(KDE_SITE)/plasma/{pkgver}/kmenuedit-{pkgver}.tar.xz"
sha256 = "2d9801b7f89988046472c2b32385d848a0a98095fb178d58d6e3b5090ced9b8b"
hardening = ["vis"]
