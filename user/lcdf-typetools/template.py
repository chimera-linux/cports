pkgname = "lcdf-typetools"
pkgver = "2.110"
pkgrel = 0
build_style = "gnu_configure"
# configure defaults to requiring kpathsea and hard-fails if not found;
# kpathsea/TeX Live isn't packaged in cports
configure_args = ["--without-kpathsea"]
hostmakedepends = ["automake"]
pkgdesc = "Utilities for manipulating OpenType and PostScript Type 1 fonts"
license = "GPL-2.0-only"
url = "https://www.lcdf.org/type"
source = f"{url}/lcdf-typetools-{pkgver}.tar.gz"
sha256 = "517f9ee879208679d3224a14d5e6eb20598fc648d5c3562708083d003088a934"


def post_install(self):
    self.install_license("COPYING")
