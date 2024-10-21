pkgname = "swig"
pkgver = "4.3.0"
pkgrel = 0
build_style = "gnu_configure"
# broken
configure_gen = []
hostmakedepends = ["byacc"]
makedepends = ["zlib-ng-compat-devel", "pcre2-devel"]
pkgdesc = "Simplified Wrapper and Interface Generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.swig.org"
source = f"$(SOURCEFORGE_SITE)/swig/swig-{pkgver}.tar.gz"
sha256 = "f7203ef796f61af986c70c05816236cbd0d31b7aa9631e5ab53020ab7804aa9e"
hardening = ["!vis", "!cfi"]
# broken check target?
options = ["!check"]
