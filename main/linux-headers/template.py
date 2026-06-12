pkgname = "linux-headers"
pkgver = "7.0.12"
pkgrel = 0
hostmakedepends = ["perl"]
pkgdesc = "Linux API headers for userland development"
license = "GPL-2.0-only"
url = "https://www.kernel.org"
source = f"$(KERNEL_SITE)/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "57edc9a41efc1ca6b797afa8f4a587a30da2af6bca7356eb56e1e1a4ada265da"
# nothing to test
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        _arch = "x86_64"
    case "aarch64":
        _arch = "arm64"
    case "ppc64le" | "ppc64" | "ppc":
        _arch = "powerpc"
    case "riscv64":
        _arch = "riscv"
    case "armhf" | "armv7":
        _arch = "arm"
    case "loongarch64" | "loongarch64":
        _arch = "loongarch"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"


def build(self):
    self.do(
        "make",
        "ARCH=" + _arch,
        "CC=clang",
        "HOSTCC=clang",
        "mrproper",
        "headers",
    )

    # remove extra files and drm headers
    for fn in self.find(".", ".*", files=True):
        self.rm(fn)

    self.rm("usr/include/Makefile")
    self.rm("usr/include/drm", recursive=True)


def install(self):
    self.install_files("usr/include", "usr")
