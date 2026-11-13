pkgname = "knewstuff"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
# fails in chroot for some reason
make_check_args = ["-E", "atticaprovidertest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "attica-devel",
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kpackage-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "syndication-devel",
]
depends = ["kirigami"]
pkgdesc = "Framework for downloading/sharing additional app data"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/knewstuff-{pkgver}.tar.xz"
sha256 = "91ee15856bb831d1f4022fb45c8b29b15be6e9330bbc8447fadeee9d6f16ab27"
hardening = ["vis"]


@subpackage("knewstuff-devel")
def _(self):
    self.depends += [
        "attica-devel",
        "kcoreaddons-devel",
        "qt6-qtbase-devel",
    ]

    return self.default_devel()
