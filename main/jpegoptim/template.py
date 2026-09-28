pkgname = "jpegoptim"
pkgver = "1.5.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-arith"]
# weird missing templates for configure.in
configure_gen = []
make_dir = "."
makedepends = ["libjpeg-turbo-devel"]
pkgdesc = "Utility for optimising jpeg files"
license = "GPL-3.0-or-later"
url = "https://github.com/tjko/jpegoptim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "661a808dfffa933d78c6beb47a2937d572b9f03e94cbaaab3d4c0d72f410e9be"
hardening = ["vis", "!cfi"]
# no tests
options = ["!check"]
