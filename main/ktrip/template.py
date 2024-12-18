pkgname = "ktrip"
pkgver = "24.12.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/ktrip"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ktrip-{pkgver}.tar.xz"
sha256 = "cc263be64a0eba68a81f6ddbc0c1b5a8bd007cc2ba0f6e6f0547ae8b6716eaaa"
