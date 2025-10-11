pkgname = "cups-filters"
pkgver = "2.0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO mupdf deptree
    "--disable-mutool",
    "--with-shell=/bin/sh",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "avahi-devel",
    "cups-devel",
    "libcupsfilters-devel",
    "libppd-devel",
    "linux-headers",
]
depends = ["cups"]
install_if = [self.with_pkgver("brlaser")]
pkgdesc = "Filters, backends, utilities for CUPS"
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/cups-filters"
source = f"https://github.com/OpenPrinting/cups-filters/releases/download/{pkgver}/cups-filters-{pkgver}.tar.xz"
sha256 = "39e71de3ce06762b342749f1dc7cba6817738f7bf4d322c1bb9ab10b8569ab80"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("COPYING")
