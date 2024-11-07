pkgname = "colord-kde"
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
sha256 = "ae895e5cfdc3e77bf88a482c034a7748d00a4ce7d74d522cb94b68be876a02d2"
hardening = ["vis"]
