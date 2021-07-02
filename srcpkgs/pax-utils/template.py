pkgname = "pax-utils"
version = "1.3.2"
revision = 1
build_style = "gnu_configure"
configure_args = ["--with-caps"]
hostmakedepends = ["pkgconf"]
makedepends = ["libcap-devel"]
short_desc = "PaX aware and related utilities for ELF binaries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
homepage = "https://cgit.gentoo.org/proj/pax-utils.git"
distfiles = [f"https://gentoo.osuosl.org/distfiles/{pkgname}-{version}.tar.xz"]
checksum = ["02eba0c305ad349ad6ff1f30edae793061ce95680fd5bdee0e14caf731dee1e7"]

def post_install(self):
    # bash scripts
    (self.destdir / "usr/bin/lddtree").unlink(missing_ok = True)
    (self.destdir / "usr/bin/symtree").unlink(missing_ok = True)
