pkgname = "swig"
pkgver = "4.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["byacc"]
makedepends = ["zlib-devel", "pcre-devel"]
pkgdesc = "Simplified Wrapper and Interface Generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.swig.org"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d53be9730d8d58a16bf0cbd1f8ac0c0c3e1090573168bfa151b01eb47fa906fc"
# broken check target?
options = ["!check", "lto"]
