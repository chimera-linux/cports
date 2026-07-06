pkgname = "kmailtransport"
pkgver = "26.04.3"
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
sha256 = "fea7cd107ddc2199e8c104eba00eb8469ffaaccd67ce4e403917971d23e4c675"


@subpackage("kmailtransport-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()
