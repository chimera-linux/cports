pkgname = "swig"
pkgver = "4.2.0"
pkgrel = 0
build_style = "gnu_configure"
# broken
configure_gen = []
hostmakedepends = ["byacc"]
makedepends = ["zlib-devel", "pcre2-devel"]
pkgdesc = "Simplified Wrapper and Interface Generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.swig.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "261ca2d7589e260762817b912c075831572b72ff2717942f75b3e51244829c97"
hardening = ["!cfi"]  # TODO
# broken check target?
options = ["!check"]
