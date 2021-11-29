pkgname = "pax-utils"
pkgver = "1.3.3"
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
sha256 = "eeca7fbd98bc66bead4a77000c2025d9f17ea8201b84245882406ce00b9b6b14"
# needs python elftools
options = ["!check"]
