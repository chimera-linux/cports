pkgname = "ksmtp"
pkgver = "25.08.3"
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
sha256 = "150741807723f1cee46bc1e86394d785fefd7df822523d5fe53832a2e415cce6"


@subpackage("ksmtp-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]
    return self.default_devel()
