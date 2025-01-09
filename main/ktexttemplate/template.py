pkgname = "ktexttemplate"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = ["qt6-qtdeclarative-devel"]
pkgdesc = "KDE library for text templates"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/ktexttemplate/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexttemplate-{pkgver}.tar.xz"
sha256 = "4c5f6c71ee1895285a97e1329a60c6a0dc5f8aca4875970f4bdf7442f211c8a9"
hardening = ["vis"]


@subpackage("ktexttemplate-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
