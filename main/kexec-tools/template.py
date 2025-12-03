pkgname = "kexec-tools"
pkgver = "2.0.32"
pkgrel = 0
archs = ["aarch64", "armhf", "armv7", "ppc64", "ppc64le", "x86_64"]
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
makedepends = [
    "linux-headers",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Tools for kexec"
license = "GPL-2.0-only"
url = "https://kernel.org/pub/linux/utils/kernel/kexec"
source = f"$(KERNEL_SITE)/utils/kernel/kexec/kexec-tools-{pkgver}.tar.xz"
sha256 = "8f81422a5fd2362cf6cb001b511e535565ed0f32c2f4451fb5eb68fed6710a5d"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # useless test program
    if self.profile().arch == "x86_64":
        self.uninstall("usr/lib/kexec-tools")
