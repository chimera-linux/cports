pkgname = "breeze-gtk"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "breeze",
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "python-cairo",
    "sassc",
]
makedepends = ["breeze-devel", "qt6-qtbase-devel"]
pkgdesc = "KDE Breeze widget theme for GTK"
license = "CC0-1.0"
url = "https://invent.kde.org/plasma/breeze-gtk"
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/breeze-gtk-{pkgver}.tar.xz"
sha256 = "ead373b1f7fc609ce75e0313f423d11a55d333217659735d48f329a70e52f7fe"
