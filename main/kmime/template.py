pkgname = "kmime"
pkgver = "6.30.0"
pkgrel = 0
build_style = "cmake"
# fails on ppc64le with wrong encoding
make_check_args = ["-E", "(headertest|messagetest)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "qt6-qttools-devel",
]
makedepends = [
    "kcodecs-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE library for mail messages"
license = "LGPL-2.0-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kmime-{pkgver}.tar.xz"
sha256 = "2969a5ef484e98f91bf78e88c98a9d613bdd3bb86ac154ceece0557b70f373bc"


@subpackage("kmime-devel")
def _(self):
    self.depends += [
        "kcodecs-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
