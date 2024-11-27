pkgname = "smartmontools"
pkgver = "7.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-scriptpath=/usr/local/bin:/usr/bin",
]
hostmakedepends = ["automake"]
makedepends = [
    "libcap-ng-devel",
    "linux-headers",
]
pkgdesc = "Utilities for SMART-enabled drives"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.smartmontools.org"
source = f"$(SOURCEFORGE_SITE)/smartmontools/smartmontools-{pkgver}.tar.gz"
sha256 = "e9a61f641ff96ca95319edfb17948cd297d0cd3342736b2c49c99d4716fb993d"
hardening = ["vis", "cfi"]


def post_install(self):
    # TODO: patch in readiness
    self.install_service(self.files_path / "smartd")
