pkgname = "sddm-kcm"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knewstuff-devel",
    "kservice",
    "qt6-qtdeclarative-devel",
]
depends = ["sddm"]
pkgdesc = "KDE Login Screen (SDDM) KCM"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/sddm-kcm"
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/sddm-kcm-{pkgver}.tar.xz"
sha256 = "81516251ee8f147b138971ee4262c9b6e57dcee670168b358678d70cff5abc40"
