pkgname = "thin-provisioning-tools"
pkgver = "0.9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-testing"]
make_cmd = "gmake"
make_dir = "." # otherwise tests will not build
make_check_target = "test"
# gawk needed for manpage generation
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool", "gawk"]
makedepends = ["boost-devel", "libexpat-devel", "libaio-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a2508d9933ed8a3f6c8d302280d838d416668a1d914a83c4bd0fb01eaf0676e8"
hardening = ["vis", "cfi"]
# needs gtest...
options = ["!check"]

def init_configure(self):
    self.make_install_args += [
        f"BINDIR={self.chroot_destdir}/usr/bin",
        f"MANDIR={self.chroot_destdir}/usr/share/man",
    ]

def pre_configure(self):
    self.do("autoreconf", "-if")
