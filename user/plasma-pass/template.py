pkgname = "plasma-pass"
pkgver = "1.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "libplasma-devel",
    "oath-toolkit-devel",
    "plasma5support-devel",
    "qgpgme-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Plasma applet for the Pass password manager"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-pass"
source = f"$(KDE_SITE)/plasma-pass/plasma-pass-{pkgver}.tar.xz"
sha256 = "5a88985dc522ca3287f13ed989609a93871996d4e8c5b0a41594e2d3a2fe8f2a"
hardening = ["cfi", "vis"]
