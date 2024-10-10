pkgname = "signon-kwallet-extension"
pkgver = "24.08.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/network/signon-kwallet-extension"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/signon-kwallet-extension-{pkgver}.tar.xz"
sha256 = "d58d829db548f26c97b41c20a864777700ef44c4424a6b341002c84590980ffc"
hardening = ["vis"]
