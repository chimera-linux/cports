pkgname = "signon-kwallet-extension"
pkgver = "25.12.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kwallet-devel",
    "signond-devel",
]
pkgdesc = "KWallet integration for signond"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/network/signon-kwallet-extension"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/signon-kwallet-extension-{pkgver}.tar.xz"
sha256 = "12ca0e75ce8c7656920f9476796ee32a858785ed6b42108ae05f55e8953c5e8a"
hardening = ["vis"]
