pkgname = "kdav"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
# hangs forever
make_check_args = ["-E", "davitemfetchjob"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE DAV library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdav/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdav-{pkgver}.tar.xz"
)
sha256 = "2e8eff3e8c35001688807a97e490a6e7851a7a1a1fdf72df5559863b8612903d"


@subpackage("kdav-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
