pkgname = "ksmtp"
pkgver = "25.12.1"
pkgrel = 0
build_style = "cmake"
# needs networking
make_check_args = ["-E", "smtptest"]
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
    "libsasl-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE SMTP library"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/kdepim/ksmtp/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksmtp-{pkgver}.tar.xz"
sha256 = "3fa5de3c7fd85f9b4a99a046b74a99fd08b2083904cfbb31995c0292b92880e0"


@subpackage("ksmtp-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
