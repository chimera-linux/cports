pkgname = "linux-headers"
pkgver = "6.9"
pkgrel = 0
hostmakedepends = ["gmake", "perl"]
pkgdesc = "Linux API headers for userland development"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://www.kernel.org"
source = f"$(KERNEL_SITE)/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "24fa01fb989c7a3e28453f117799168713766e119c5381dac30115f18f268149"
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


def do_build(self):
    self.do(
        "gmake",
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


def do_install(self):
    self.install_files("usr/include", "usr")
