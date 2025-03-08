pkgname = "kio-admin"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kio-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE KIO admin:// protocol implementation"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/system/kio-admin"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-admin-{pkgver}.tar.xz"
sha256 = "72bbed31f4fffad9420299796ee4c8a072dd66ee30c7907f7ca2cc05395a4811"
hardening = ["vis"]
