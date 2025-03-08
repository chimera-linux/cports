pkgname = "kalk"
pkgver = "24.12.3"
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
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://apps.kde.org/kalk"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kalk-{pkgver}.tar.xz"
sha256 = "3027a1bd7677b571f87a400b144130a52a8fb1e6da443353e5149d5f935c9f77"
hardening = ["vis"]
