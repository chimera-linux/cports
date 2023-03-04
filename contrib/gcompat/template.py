pkgname = "gcompat"
pkgver = "1.1.0"
pkgrel = 0

match self.profile().arch:
    case "ppc64le":
        _glibc = "ld64.so.2"
        _musl = "ld-musl-powerpc64le.so.1"
    case "ppc64":
        _glibc = "ld64.so.2"
        _musl = "ld-musl-powerpc64.so.1"
    case "aarch64":
        _glibc = "ld-linux-aarch64.so.1"
        _musl = "ld-musl-aarch64.so.1"
    case "x86_64":
        _glibc = "ld-linux-x86-64.so.2"
        _musl = "ld-musl-x86_64.so.1"
    case "riscv64":
        _glibc = "ld-linux-riscv64-lp64d.so.1"
        _musl = "ld-musl-riscv64.so.1"

hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libunwind-devel-static", "musl-devel-static", "libucontext-devel", "libatomic-chimera-devel-static"]
make_cmd = "gmake"
make_build_args = [f"LINKER_PATH=/usr/lib/{_musl}", f"LOADER_NAME={_glibc}", "LIBGCOMPAT_PATH=/usr/lib/libgcompat.so.0",
                   f"LOADER_PATH=/usr/lib/{_glibc}", "WITH_LIBUCONTEXT=1"]
make_install_args = make_build_args
build_style = "makefile"
pkgdesc = "GNU C Library Compatibility Layer for Adélie Linux"
maintainer = "eater <=@eater.me>"
license = "ISC"
url = "https://git.adelielinux.org/adelie/gcompat"
source = f"https://git.adelielinux.org/adelie/gcompat/-/archive/{pkgver}/gcompat-{pkgver}.tar.gz"
sha256 = "82e56d2ecda3f11a93efe61001394a6e5db39c91127d0812d7ad5b0bda558010"
# no rules defined for check
options = ["!check"]


def pre_install(self):
    # make install doesn't create the dirs and dies
    self.install_dir('usr/lib')
