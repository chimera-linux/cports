pkgname = "msmtp"
pkgver = "1.8.28"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = [
    "gnutls-devel",
    "libidn2-devel",
    "libsecret-devel",
]
checkdepends = ["bash"]
pkgdesc = "SMTP client"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://marlam.de/msmtp"
source = f"{url}/releases/msmtp-{pkgver}.tar.xz"
sha256 = "3a57f155f54e4860f7dd42138d9bea1af615b99dfab5ab4cd728fc8c09a647a4"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "msmtpd")
