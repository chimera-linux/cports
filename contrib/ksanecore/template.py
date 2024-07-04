pkgname = "ksanecore"
pkgver = "24.05.2"
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
sha256 = "a9439b6f686363fa32c6f4a5287e8c5df86547015e64b88587691d64492ec95d"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
