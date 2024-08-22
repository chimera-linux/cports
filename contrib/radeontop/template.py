pkgname = "radeontop"
pkgver = "1.4"
pkgrel = 2
build_style = "makefile"
make_use_env = True
hostmakedepends = ["gettext", "pkgconf"]
makedepends = ["linux-headers", "libdrm-devel", "libxcb-devel", "ncurses-devel"]
pkgdesc = "Radeon GPU utilization tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://github.com/clbr/radeontop"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2c1e2aace1a749d8e4530047ce245004e0f7d1d32a99037917e03d83e60f7ad1"
env = {"VERSION": pkgver}
# no tests
options = ["!check"]
