pkgname = "ksmtp"
pkgver = "25.04.1"
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
sha256 = "42ba6db84b35ff6b50ee58ba4da14eccda44b60242b4095d53f46129d6dbc47d"


@subpackage("ksmtp-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
