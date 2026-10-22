pkgname = "ksshaskpass"
pkgver = "6.8.1"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
pkgdesc = "KDE askpass helper"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/ksshaskpass"
source = f"$(KDE_SITE)/plasma/{pkgver}/ksshaskpass-{pkgver}.tar.xz"
sha256 = "abbc3ad10cd1cdebefd20bdad87224b7dc305c09b8863b6e90c6c838bf3c3122"
