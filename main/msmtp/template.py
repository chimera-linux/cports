pkgname = "msmtp"
pkgver = "1.8.30"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "gnutls-devel",
    "libidn2-devel",
    "libsecret-devel",
]
checkdepends = ["bash"]
pkgdesc = "SMTP client"
license = "GPL-3.0-or-later"
url = "https://marlam.de/msmtp"
source = f"{url}/releases/msmtp-{pkgver}.tar.xz"
sha256 = "f826a3c500c4dfeed814685097cead9b2b3dca5a2ec3897967cb9032570fa9ab"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "msmtpd")
