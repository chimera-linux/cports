pkgname = "ktrip"
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
    "kcrash-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kpublictransport-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kirigami-addons"]
pkgdesc = "KDE trip planner"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ktrip"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ktrip-{pkgver}.tar.xz"
sha256 = "9eb032811755f04d628d5a173c07da9ef92b554087d53d203cd56a630cf09b28"
