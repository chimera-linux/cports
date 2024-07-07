pkgname = "kexec-tools"
pkgver = "2.0.28"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "gmake", "libtool"]
makedepends = ["linux-headers", "xz-devel", "zlib-ng-compat-devel"]
pkgdesc = "Tools for kexec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org/pub/linux/utils/kernel/kexec"
source = f"$(KERNEL_SITE)/utils/kernel/kexec/kexec-tools-{pkgver}.tar.xz"
sha256 = "d2f0ef872f39e2fe4b1b01feb62b0001383207239b9f8041f98a95564161d053"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # useless test program
    self.uninstall("usr/lib/kexec-tools")
