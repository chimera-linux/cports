pkgname = "kmenuedit"
pkgver = "6.4.5"
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
sha256 = "610f07cd3a26c1618e2a7c31ce9011b28b3af0df5da65eb0100a7e8f08c8942f"
hardening = ["vis"]
