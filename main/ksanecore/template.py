pkgname = "ksanecore"
pkgver = "24.12.2"
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
sha256 = "10832182393f7a63d4eb223f1fafdada1c830b4cc88230e94c60e9337fbf84c3"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
