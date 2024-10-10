pkgname = "kontrast"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "futuresql-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kirigami-addons-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE contrast inspection tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kontrast"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kontrast-{pkgver}.tar.xz"
sha256 = "ed60b1e229fa4a2b0511c4e8a27a19479b69274f69b18f77820922cded0b5104"
