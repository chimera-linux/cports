pkgname = "kexec-tools"
pkgver = "2.0.31"
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
sha256 = "8a8f350ddc66e1c905a3ab525a7e9ba96c81e04e70ef69397b0155b67b922c31"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # useless test program
    if self.profile().arch == "x86_64":
        self.uninstall("usr/lib/kexec-tools")
