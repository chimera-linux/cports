pkgname = "kdenetwork-filesharing"
pkgver = "25.12.2"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
sha256 = "69a4f7745d48a6b0cea19c4d987149e4e543c46b6eaa15d3d19c7857e4f0ae70"
