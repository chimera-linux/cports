pkgname = "ktrip"
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
    "kirigami-addons-devel",
    "kpublictransport-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kirigami-addons"]
pkgdesc = "KDE trip planner"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ktrip"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ktrip-{pkgver}.tar.xz"
sha256 = "4fe89426f5a261b2fc33de30adbc0a5405321b13e5e1d644a034aa772ac49b37"
