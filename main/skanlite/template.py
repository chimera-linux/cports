pkgname = "skanlite"
pkgver = "24.12.0"
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
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kxmlgui-devel",
    "libksane-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE scanning application for images"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/skanlite"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/skanlite-{pkgver}.tar.xz"
sha256 = "e4f9850fc9b9cecd04d695abe87cbf91a32b0ee58bf56ccdf13470727ab322e6"
