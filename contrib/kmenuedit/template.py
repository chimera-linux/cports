pkgname = "kmenuedit"
pkgver = "6.0.5"
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
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemviews-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "sonnet-devel",
]
pkgdesc = "KDE menu editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://invent.kde.org/plasma/kmenuedit"
source = f"$(KDE_SITE)/plasma/{pkgver}/kmenuedit-{pkgver}.tar.xz"
sha256 = "9aa1d39724cba1e7b8f6ded8c490acdfe11598ed368c28e9aa86572698e359f8"
# CFI: check
hardening = ["vis", "!cfi"]
