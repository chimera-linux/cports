pkgname = "jpegoptim"
pkgver = "1.5.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-arith"]
# weird missing templates for configure.in
configure_gen = []
make_dir = "."
makedepends = ["libjpeg-turbo-devel"]
pkgdesc = "Utility for optimising jpeg files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/tjko/jpegoptim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "90a309d1c092de358bb411d702281ac3039b489d03adb0bc3c4ef04cf0067d38"
hardening = ["vis", "!cfi"]
# no tests
options = ["!check"]
