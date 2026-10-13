pkgname = "kalk"
pkgver = "26.08.2"
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
sha256 = "bb0062cd9d550d5b77f10060e739a4fe70c7d43f5ef54ca07f0a93f77a22ce11"
hardening = ["vis"]
