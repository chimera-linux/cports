pkgname = "attica"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
# requires network access and passes in cbuild chroot
make_check_args = ["-E", "providertest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
]
pkgdesc = "Freedesktop Open Collaboration Services (OCS) binding for Qt"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/attica/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/attica-{pkgver}.tar.xz"
sha256 = "f36c2eacbcad8c08036e9f7525144bec9f7c5d86f1150d49f9db9e3dc14abf45"
hardening = ["vis"]


@subpackage("attica-devel")
def _(self):
    return self.default_devel()
