pkgname = "grantlee-editor"
pkgver = "25.12.1"
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
sha256 = "055f90abdd8618d193861af00c2b1c24f70458fd521d702718a258f9fe253261"
