pkgname = "kmbox"
pkgver = "24.12.3"
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
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmbox/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmbox-{pkgver}.tar.xz"
sha256 = "fe0ca441094a71d9169e4bf69362af1dee9dc2e67e08ada3251c6bd25dcb9720"


@subpackage("kmbox-devel")
def _(self):
    self.depends += ["kmime-devel"]
    return self.default_devel()
