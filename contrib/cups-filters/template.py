pkgname = "cups-filters"
pkgver = "2.0.0"
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
    "libtool",
    "pkgconf",
]
makedepends = [
    "avahi-devel",
    "cups-devel",
    "libcupsfilters-devel",
    "libppd-devel",
    "linux-headers",
]
depends = ["cups"]
pkgdesc = "Filters, backends, utilities for CUPS"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND custom:gpl-exception"
url = "https://github.com/OpenPrinting/cups-filters"
source = f"https://github.com/OpenPrinting/cups-filters/releases/download/{pkgver}/cups-filters-{pkgver}.tar.xz"
sha256 = "b5152e3dd148ed73835827ac2f219df7cf5808dbf9dbaec2aa0127b44de800d8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
