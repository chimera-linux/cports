pkgname = "msmtp"
pkgver = "1.8.26"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "pkgconf"]
makedepends = ["gnutls-devel", "libsecret-devel", "libidn2-devel"]
pkgdesc = "SMTP client"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://marlam.de/msmtp"
source = f"{url}/releases/msmtp-{pkgver}.tar.xz"
sha256 = "6cfc488344cef189267e60aea481f00d4c7e2a59b53c6c659c520a4d121f66d8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "msmtpd")
