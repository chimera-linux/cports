pkgname = "colord-kde"
pkgver = "24.12.2"
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
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "lcms2-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE colord integration"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/graphics/colord-kde"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/colord-kde-{pkgver}.tar.xz"
sha256 = "37a35ce1e9b25bd5afc92de67c9a3753b26cd294603dacb93930d129079a8388"
hardening = ["vis"]
