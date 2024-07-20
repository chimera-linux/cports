pkgname = "kexec-tools"
pkgver = "2.0.29"
pkgrel = 0
archs = ["aarch64", "armhf", "armv7", "ppc64", "ppc64le", "x86_64"]
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "gmake", "libtool"]
makedepends = ["linux-headers", "xz-devel", "zlib-ng-compat-devel"]
pkgdesc = "Tools for kexec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org/pub/linux/utils/kernel/kexec"
source = f"$(KERNEL_SITE)/utils/kernel/kexec/kexec-tools-{pkgver}.tar.xz"
sha256 = "67b1ac503aade45a54db0bc79228a8830a35d5d4f83cee932cff3e7a81a4a9ec"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # useless test program
    if self.profile().arch == "x86_64":
        self.uninstall("usr/lib/kexec-tools")
