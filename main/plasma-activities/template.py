pkgname = "plasma-activities"
pkgver = "6.3.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Core components for KDE's Activity Manager"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/plasma/plasma-activities"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-activities-{pkgver}.tar.xz"
sha256 = "9a20300f30ad9d785c1e20b12b20fe0259e83947b550d10ea63ab1f91f1dd675"
hardening = ["vis"]


@subpackage("plasma-activities-devel")
def _(self):
    return self.default_devel()
