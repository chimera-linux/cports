pkgname = "swig"
pkgver = "4.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["byacc"]
makedepends = ["zlib-devel", "pcre2-devel"]
pkgdesc = "Simplified Wrapper and Interface Generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.swig.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d6a9a8094e78f7cfb6f80a73cc271e1fe388c8638ed22668622c2c646df5bb3d"
hardening = ["!cfi"] # TODO
# broken check target?
options = ["!check"]
