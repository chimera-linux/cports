pkgname = "colord-kde"
pkgver = "24.12.0"
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
sha256 = "f03c6237372fa40c875a69df978375c08478f239fcbde048fdb46431b2e7e0e4"
hardening = ["vis"]
