pkgname = "kdav"
pkgver = "6.7.0"
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
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdav-{pkgver}.tar.xz"
)
sha256 = "6629f2af0042eb1e0dc0c08b5180ac7b48dae6b5999e1dd0b678aed8b874c1d7"


@subpackage("kdav-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
