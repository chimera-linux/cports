pkgname = "swig"
pkgver = "4.2.1"
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
sha256 = "fa045354e2d048b2cddc69579e4256245d4676894858fcf0bab2290ecf59b7d8"
hardening = ["!cfi"]  # TODO
# broken check target?
options = ["!check"]
