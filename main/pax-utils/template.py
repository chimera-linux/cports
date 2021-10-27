pkgname = "pax-utils"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-caps", "--without-python"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "python"]
depends = ["bash"]
pkgdesc = "PaX aware and related utilities for ELF binaries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://cgit.gentoo.org/proj/pax-utils.git"
source = f"https://gentoo.osuosl.org/distfiles/{pkgname}-{pkgver}.tar.xz"
sha256 = "02eba0c305ad349ad6ff1f30edae793061ce95680fd5bdee0e14caf731dee1e7"
# needs python elftools
options = ["!check"]
