pkgname = "kexec-tools"
pkgver = "2.0.30"
pkgrel = 0
archs = ["aarch64", "armhf", "armv7", "ppc64", "ppc64le", "x86_64"]
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
makedepends = ["linux-headers", "xz-devel", "zlib-ng-compat-devel"]
pkgdesc = "Tools for kexec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org/pub/linux/utils/kernel/kexec"
source = f"$(KERNEL_SITE)/utils/kernel/kexec/kexec-tools-{pkgver}.tar.xz"
sha256 = "748a5fa7af27a8059d1de907bddfc32ac530c7189b5770c83e6f3d898d82124e"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # useless test program
    if self.profile().arch == "x86_64":
        self.uninstall("usr/lib/kexec-tools")
