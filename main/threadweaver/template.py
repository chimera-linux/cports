pkgname = "threadweaver"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "KDE Multithreading helper library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/threadweaver/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/threadweaver-{pkgver}.tar.xz"
sha256 = "136a636a33ccfa9a375a2e1ee503760a0a910002b972be0eef20352eb106bb84"
hardening = ["vis"]


@subpackage("threadweaver-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
