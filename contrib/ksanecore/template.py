pkgname = "ksanecore"
pkgver = "24.05.0"
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
sha256 = "ca4f80b9b7d7c26483d3ebd7279a7f6b0e08d17c9419dde061780b3bfbc115bd"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
