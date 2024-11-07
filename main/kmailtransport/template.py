pkgname = "kmailtransport"
pkgver = "24.08.3"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kmailtransport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kmailtransport-{pkgver}.tar.xz"
)
sha256 = "bb1afa02df447753eed44026aa90c313d42401644ad1032c6c91371a91362e69"


@subpackage("kmailtransport-devel")
def _(self):
    self.depends += ["kconfig-devel"]
    return self.default_devel()
