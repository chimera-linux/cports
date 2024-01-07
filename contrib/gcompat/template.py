pkgname = "gcompat"
pkgver = "1.1.0"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "musl-devel-static",
    "libucontext-devel",
]
pkgdesc = "Glibc compatibility shim for musl"
maintainer = "eater <=@eater.me>"
license = "ISC"
url = "https://git.adelielinux.org/adelie/gcompat"
source = f"https://git.adelielinux.org/adelie/gcompat/-/archive/{pkgver}/gcompat-{pkgver}.tar.gz"
sha256 = "82e56d2ecda3f11a93efe61001394a6e5db39c91127d0812d7ad5b0bda558010"
# no test suite
options = ["!check", "brokenlinks"]

match self.profile().arch:
    case "ppc64le":
        _glibc = "ld64.so.2"
        _musl = "ld-musl-powerpc64le.so.1"
    case "ppc64":
        _glibc = "ld64.so.2"
        _musl = "ld-musl-powerpc64.so.1"
    case "ppc":
        _glibc = "ld.so.1"
        _musl = "ld-musl-powerpc.so.1"
    case "aarch64":
        _glibc = "ld-linux-aarch64.so.1"
        _musl = "ld-musl-aarch64.so.1"
    case "x86_64":
        _glibc = "ld-linux-x86-64.so.2"
        _musl = "ld-musl-x86_64.so.1"
    case "riscv64":
        _glibc = "ld-linux-riscv64-lp64d.so.1"
        _musl = "ld-musl-riscv64.so.1"
    case _:
        _glibc = ""
        _musl = ""
        broken = f"unknown architecture {self.profile().arch}"

make_build_args = [
    f"LOADER_NAME={_glibc}",
    f"LOADER_PATH=/usr/lib/{_glibc}",
    f"LINKER_PATH=/usr/lib/{_musl}",
    "LIBGCOMPAT_PATH=/usr/lib/libgcompat.so.0",
    "WITH_LIBUCONTEXT=1",
]
make_install_args = list(make_build_args)


def pre_install(self):
    # make install doesn't create the dirs and dies
    self.install_dir("usr/lib")


def post_install(self):
    self.install_license("LICENSE")
    # compat links
    ws = self.profile().wordsize
    self.install_link("lib", f"lib{ws}")
    self.install_link("lib", f"usr/lib{ws}")
