pkgname = "ksmtp"
pkgver = "25.04.0"
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
sha256 = "28410ecf9a86bbb798875853d16e72274ba85962f7a54016e8d6aa0fdcab4f0d"


@subpackage("ksmtp-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
