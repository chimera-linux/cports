pkgname = "dfu-programmer"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
# broken
configure_gen = []
make_dir = "."
makedepends = ["libusb-devel"]
pkgdesc = "Command-line programmer for Atmel USB microcontrollers"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://dfu-programmer.github.io"
source = f"https://github.com/dfu-programmer/dfu-programmer/releases/download/v{pkgver}/dfu-programmer-{pkgver}.tar.gz"
sha256 = "844e469be559657bc52c9d9d03c30846acd11ffbb1ddd42438fa8af1d2b8587d"
hardening = ["vis", "cfi"]
