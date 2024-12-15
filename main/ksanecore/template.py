pkgname = "ksanecore"
pkgver = "24.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "gperf",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
    "sane-backends-devel",
]
pkgdesc = "KDE integration for SANE"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries-ksanecore"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksanecore-{pkgver}.tar.xz"
sha256 = "3d5275d182be9b869eb26688195abe37bdc7c55dac669377a9bce7d847440829"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
