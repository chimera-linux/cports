pkgname = "msmtp"
pkgver = "1.8.27"
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
sha256 = "94030580a63a747faa0a3b9b1b264ae355aad33a4d94b832bfeb5b21633c965e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "msmtpd")
