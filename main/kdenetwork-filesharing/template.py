pkgname = "kdenetwork-filesharing"
pkgver = "25.04.1"
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
sha256 = "6350b0d5d71821c53d4b3fb007ec7e386c933661a42fc6402d1d975a5132124e"
