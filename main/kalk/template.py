pkgname = "kalk"
pkgver = "26.08.0"
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
sha256 = "0952c0d918fa962015fb8c0f9777beb9b85d8eb0a2a0351797a19c1a7815a88b"
hardening = ["vis"]
