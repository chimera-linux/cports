pkgname = "signon-kwallet-extension"
pkgver = "25.08.3"
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
sha256 = "47e79edfdb97d9240e22ed9fa624ebac3cd219e4a2ee770c6869b869b53b9aff"
hardening = ["vis"]
