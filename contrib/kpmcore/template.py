pkgname = "kpmcore"
pkgver = "24.05.2"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    "fdisk",
    "smartmontools",
]
pkgdesc = "KDE library for partition management"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpmcore-{pkgver}.tar.xz"
sha256 = "8e8646bfe990834acbbe56149015aaecd3099cc2e9115ac7426a2d88747735db"
hardening = ["vis", "!cfi"]


@subpackage("kpmcore-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
