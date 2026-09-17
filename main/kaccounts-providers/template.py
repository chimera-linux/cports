pkgname = "kaccounts-providers"
pkgver = "26.08.1"
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
sha256 = "59d70593a7b8917500fa65ee8ec6c876d30ea2213d1a7a454aaff7d1da1fccb1"
hardening = ["vis"]
options = ["etcfiles"]


if self.profile.arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
