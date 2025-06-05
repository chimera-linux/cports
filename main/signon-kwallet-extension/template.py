pkgname = "signon-kwallet-extension"
pkgver = "25.04.2"
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
sha256 = "e8032e1862d93c0b3e0ca82e97e719be7e261647cae0b66f46730ed359ac8112"
hardening = ["vis"]
