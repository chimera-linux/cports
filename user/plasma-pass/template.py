pkgname = "plasma-pass"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "gpgme-qt-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "libplasma-devel",
    "oath-toolkit-devel",
    "plasma5support-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Plasma applet for the Pass password manager"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-pass"
source = f"$(KDE_SITE)/plasma-pass/plasma-pass-{pkgver}.tar.xz"
sha256 = "91b32509638ab602073816287110ac79b86ffc7f05c23b3285886f7ce6e4cd0f"
hardening = ["cfi", "vis"]
