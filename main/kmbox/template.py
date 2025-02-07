pkgname = "kmbox"
pkgver = "24.12.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kmime-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM mbox access library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmbox/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmbox-{pkgver}.tar.xz"
sha256 = "da33971bf49ffcaecef8a2f57dd6c434301b2d31ed1b761ef5e21258a39214e5"


@subpackage("kmbox-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()
