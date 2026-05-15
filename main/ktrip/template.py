pkgname = "ktrip"
pkgver = "26.04.1"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
sha256 = "80a51468c09c21b11c083d43afb695655c59ba0c4ebd996f48330b0cbaf2724c"
