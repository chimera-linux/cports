pkgname = "smartmontools"
pkgver = "7.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-scriptpath=/usr/local/bin:/usr/bin",
]
hostmakedepends = ["automake"]
makedepends = [
    "dinit-chimera",
    "libcap-ng-devel",
    "linux-headers",
]
pkgdesc = "Utilities for SMART-enabled drives"
license = "GPL-2.0-or-later"
url = "https://www.smartmontools.org"
source = f"$(SOURCEFORGE_SITE)/smartmontools/smartmontools-{pkgver}.tar.gz"
sha256 = "690b83ca331378da9ea0d9d61008c4b22dde391387b9bbad7f29387f2595f76e"
hardening = ["vis", "cfi"]


def post_install(self):
    # TODO: patch in readiness
    self.install_service(self.files_path / "smartd")
