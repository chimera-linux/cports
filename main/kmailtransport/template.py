pkgname = "kmailtransport"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cmake"
# no worthy sasl mechs
make_check_args = ["-E", "smtpjobtest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfigwidgets-devel",
    "ki18n-devel",
    "kio-devel",
    "ksmtp-devel",
    "libkgapi-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE mail transport library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmailtransport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kmailtransport-{pkgver}.tar.xz"
)
sha256 = "480ffdd92d657d2adbbf8e2fe17b3f723fc835c13fac3d519ee2651bfc2de1bf"


@subpackage("kmailtransport-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()
