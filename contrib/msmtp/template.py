pkgname = "msmtp"
pkgver = "1.8.25"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "gmake", "pkgconf"]
makedepends = [
    "gettext-devel",
    "gnutls-devel",
    "libidn2-devel",
    "libsecret-devel",
]
pkgdesc = "SMTP client with a sendmail interface"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://marlam.de/msmtp"
source = f"{url}/releases/msmtp-{pkgver}.tar.xz"
sha256 = "2dfe1dbbb397d26fe0b0b6b2e9cd2efdf9d72dd42d18e70d7f363ada2652d738"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "msmtpd")


@subpackage("msmtpd")
def _msmtpd(self):
    self.pkgdesc = f"{pkgdesc} (daemon)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/bin/msmtpd", "etc/dinit.d/msmtpd"]
