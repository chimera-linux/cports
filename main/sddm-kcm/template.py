pkgname = "sddm-kcm"
pkgver = "6.3.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/sddm-kcm"
source = f"$(KDE_SITE)/plasma/{pkgver}/sddm-kcm-{pkgver}.tar.xz"
sha256 = "ece34d6ff4485a51f9ffa95e9dc3c87811e60b06e527b184fb9ec5908e9e4450"
