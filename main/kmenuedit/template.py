pkgname = "kmenuedit"
pkgver = "6.2.4"
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
    "kcrash-devel",
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
sha256 = "174f5bfb174642b7b72445f294d410cfaccaf6573350c14af711e48dc856adf9"
hardening = ["vis"]
