pkgname = "kcharselect"
pkgver = "24.05.0"
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
    "kbookmarks-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE character picker"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kcharselect"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcharselect-{pkgver}.tar.xz"
sha256 = "ce91274b6622f8affb15a5c29d49f9e45875bfced0197e045b0d9b39fe2f6cd0"
