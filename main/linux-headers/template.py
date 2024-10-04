pkgname = "linux-headers"
pkgver = "6.11.2"
pkgrel = 0
hostmakedepends = ["perl"]
pkgdesc = "Linux API headers for userland development"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.kernel.org"
source = f"$(KERNEL_SITE)/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "ec9ef7a0b9cebb55940e1ef87a1f9e1004b10456a119dc386bb3e565b0d39c42"
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
