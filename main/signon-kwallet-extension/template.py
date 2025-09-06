pkgname = "signon-kwallet-extension"
pkgver = "25.08.0"
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
sha256 = "982899a8567ecdbe47530b53fd35c119a6cec8eacf749b6598a1d96bb49c8cfc"
hardening = ["vis"]
