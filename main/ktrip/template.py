pkgname = "ktrip"
pkgver = "26.08.3"
pkgrel = 0
build_style = "cmake"
# dies silently
make_check_args = ["-E", "ktrip-self-test"]
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
sha256 = "620addbb2b4f9246ba68234fc9ec5e8ec1acb4d9c897b43b40bc451a5cdf98bf"
