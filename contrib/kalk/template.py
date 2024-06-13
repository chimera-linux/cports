pkgname = "kalk"
pkgver = "24.05.1"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kunitconversion-devel",
    "libqalculate-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Calculator"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://apps.kde.org/kalk"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kalk-{pkgver}.tar.xz"
sha256 = "54a1023330f82ce8d146592fb5629d4a2f6813aa57ba6a98cd112a8fa7901829"
# CFI: crashes tests
hardening = ["vis", "!cfi"]
