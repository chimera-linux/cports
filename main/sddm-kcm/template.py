pkgname = "sddm-kcm"
pkgver = "6.2.2"
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
sha256 = "67c87ee531d6534c65f3fcb8c377b5ca0ff8339c935565b98986caa3fc2ac4de"
