pkgname = "kdenetwork-filesharing"
pkgver = "24.08.1"
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
    "kauth-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kwidgetsaddons-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
]
# net, testparm
depends = ["samba-common"]
pkgdesc = "KDE samba filesharing plugin"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenetwork_filesharing"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenetwork-filesharing-{pkgver}.tar.xz"
sha256 = "0dbd28611839450e79aebd9ac9b7dbc45b82b8c1cd3206d5d360d545f73f70c3"
