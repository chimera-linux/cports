pkgname = "swig"
pkgver = "4.1.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["byacc"]
makedepends = ["zlib-devel", "pcre2-devel"]
pkgdesc = "Simplified Wrapper and Interface Generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.swig.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2af08aced8fcd65cdb5cc62426768914bedc735b1c250325203716f78e39ac9b"
hardening = ["!cfi"] # TODO
# broken check target?
options = ["!check"]

configure_gen = []
