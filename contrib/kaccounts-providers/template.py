pkgname = "kaccounts-providers"
pkgver = "24.05.2"
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
    "signond-devel",
]
pkgdesc = "KDE providers for online accounts"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-providers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-providers-{pkgver}.tar.xz"
sha256 = "60ee944bec87a60da3b860584f5c61d06983455169d89b5356034ae4216dd1d5"
hardening = ["vis"]


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
