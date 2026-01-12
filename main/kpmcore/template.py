pkgname = "kpmcore"
pkgver = "25.12.1"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["smartmontools", "util-linux-fdisk"]
pkgdesc = "KDE library for partition management"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpmcore-{pkgver}.tar.xz"
sha256 = "18d1d46d1c866ed93128f58ee9850c993bc0ab375cc27ca1cd4ec20d8fcdc62b"
hardening = ["vis"]


@subpackage("kpmcore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
