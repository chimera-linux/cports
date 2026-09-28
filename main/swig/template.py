pkgname = "swig"
pkgver = "4.3.1"
pkgrel = 0
build_style = "gnu_configure"
# broken
configure_gen = []
hostmakedepends = ["byacc"]
makedepends = ["zlib-ng-compat-devel", "pcre2-devel"]
pkgdesc = "Simplified Wrapper and Interface Generator"
license = "GPL-3.0-or-later"
url = "https://www.swig.org"
source = f"$(SOURCEFORGE_SITE)/swig/swig-{pkgver}.tar.gz"
sha256 = "44fc829f70f1e17d635a2b4d69acab38896699ecc24aa023e516e0eabbec61b8"
hardening = ["!vis", "!cfi"]
# broken check target?
options = ["!check"]
