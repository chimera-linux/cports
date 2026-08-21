pkgname = "kaccounts-providers"
pkgver = "26.08.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "intltool",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kaccounts-integration-devel",
    "ki18n-devel",
    "kio-devel",
    "kpackage-devel",
    "libaccounts-qt-devel",
    "qcoro-devel",
    "signond-devel",
]
pkgdesc = "KDE providers for online accounts"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-providers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-providers-{pkgver}.tar.xz"
sha256 = "1e24a516749d1905644c6d37202ff9be88f3883a4cfc1905defae95f32582c1a"
hardening = ["vis"]
options = ["etcfiles"]


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
