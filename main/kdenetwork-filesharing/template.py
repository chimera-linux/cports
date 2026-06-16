pkgname = "kdenetwork-filesharing"
pkgver = "26.04.2"
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
    "kauth-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
]
# net, testparm
depends = ["samba-common"]
pkgdesc = "KDE samba filesharing plugin"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenetwork_filesharing"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenetwork-filesharing-{pkgver}.tar.xz"
sha256 = "d05b43808dd8de0c8b36ad6f76af447ad7525c9c37fbc2969f72dfc4a5c4712a"
