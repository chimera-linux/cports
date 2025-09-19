pkgname = "ksanecore"
pkgver = "25.08.1"
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
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries-ksanecore"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksanecore-{pkgver}.tar.xz"
sha256 = "efcbbd6ee797aee03c7d9622a150f0b4ee645f7d0856d379c2495eb25e0697c6"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
