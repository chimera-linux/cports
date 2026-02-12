pkgname = "ksmtp"
pkgver = "25.12.2"
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
sha256 = "331c237109d63c30a16293841cdfad263a0bdccb60f767831078a6ffe6489e41"


@subpackage("ksmtp-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
