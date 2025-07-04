pkgname = "grantlee-editor"
pkgver = "25.04.3"
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
    "akonadi-contacts-devel",
    "grantleetheme-devel",
    "karchive-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kimap-devel",
    "kio-devel",
    "kmime-devel",
    "ktextaddons-devel",
    "kxmlgui-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE editor for Grantlee themes"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/pim/grantlee-editor"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/grantlee-editor-{pkgver}.tar.xz"
)
sha256 = "b37a34e419d901b11ded495bfde240dbb0b7d47a978d4e76289ba3d9bbe33214"
