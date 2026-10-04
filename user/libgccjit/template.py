pkgname = "libgccjit"
pkgver = "16.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-cet",
    "--disable-fixed-point",
    "--disable-multilib",
    "--disable-nls",
    "--disable-symvers",
    "--disable-vtable-verify",
    "--disable-werror",
    "--disable-bootstrap",
    "--disable-libatomic",
    "--disable-libssp",
    "--disable-target-libssp",
    "--disable-libquadmath",
    "--disable-target-libquadmath",
    "--enable-checking=release",
    "--enable-__cxa_atexit",
    "--enable-default-pie",
    "--enable-default-ssp",
    # more languages later
    "--enable-languages=jit",
    "--enable-linker-build-id",
    "--with-matchpd-partitions=32",
    "--enable-host-shared",
    "--enable-shared",
    "--enable-threads",
    "--enable-tls",
    "--with-bugurl=https://github.com/chimera-linux/cports/issues",
    f"--with-pkgversion=Chimera {pkgver}",
    "--with-gmp",
    "--with-gnu-as",
    "--with-gnu-ld",
    "--with-isl",
    "--with-mpc",
    "--with-mpfr",
    "--with-system-zlib",
    "--with-system-zstd",
    "--with-linker-hash-style=gnu",
    "libat_cv_have_ifunc=no",
]
configure_gen = []
make_build_target = "all-gcc"
make_install_target = "jit.install-common"
make_install_args = ["-C", "gcc"]
hostmakedepends = [
    "bison",
    "flex",
    "gawk",
    "gcc",
    "perl",
    "texinfo",
]
makedepends = [
    "gmp-devel",
    "isl-devel",
    "libucontext-devel",
    "mpc-devel",
    "mpfr-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# needs the gcc libraries to drive the jit
depends = ["gcc"]
pkgdesc = "GCC JIT library"
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz"
sha256 = "e6738e29597f733270731aa90600f37ffdc045079dfc27ec7e8192cc81085c3e"
hardening = ["!int", "!format", "!var-init"]
# no tests to run
options = ["!check", "!lto", "!cross"]

_trip = self.profile.triplet
# we cannot use clang, gcc expects binutils
tools = {
    "AS": "as",
    "CC": "gcc",
    "CXX": "g++",
    "LD": "ld.bfd",
    "OBJDUMP": "gobjdump",
}

match self.profile.arch:
    case "aarch64":
        configure_args += [
            "--with-arch=armv8-a",
            "--with-abi=lp64",
        ]
    case "armv7":
        configure_args += [
            "--with-arch=armv7-a",
            "--with-tune=generic-armv7-a",
            "--with-fpu=vfpv3-d16",
            "--with-float=hard",
            "--with-abi=aapcs-linux",
            "--with-mode=thumb",
        ]
    case "ppc64":
        configure_args += [
            "--with-abi=elfv2",
            "--enable-secureplt",
            "--disable-decimal-float",
        ]
    case "ppc64le":
        configure_args += [
            "--with-abi=elfv2",
            "--enable-secureplt",
            "--disable-decimal-float",
        ]
    case "ppc":
        configure_args += [
            "--enable-secureplt",
            "--disable-decimal-float",
        ]
    case "riscv64":
        configure_args += [
            "--with-arch=rv64gc",
            "--with-abi=lp64d",
        ]
    case "loongarch64":
        configure_args += [
            "--with-arch=la64v1.0",
            "--with-abi=lp64d",
        ]


def post_patch(self):
    from cbuild.util import patch

    # we are building gcc internals using libcxx stdlib, this breaks
    # some assumptions so patch them out so we don't need to do an
    # entire bootstrap cycle again (just to build a static libcxx)
    patch.patch(self, [self.files_path / "relax-jit-libcxx.patch"])


def init_configure(self):
    cfl = self.get_cflags(shell=True)
    cxfl = self.get_cxxflags(shell=True)
    ldfl = self.get_ldflags(shell=True)
    self.env["AWK"] = "gawk"
    self.env["CFLAGS_FOR_TARGET"] = cfl
    self.env["CXXFLAGS_FOR_TARGET"] = cxfl
    self.env["LDFLAGS_FOR_TARGET"] = ldfl
    self.env["BOOT_CFLAGS"] = cfl
    self.env["BOOT_CXXFLAGS"] = cxfl
    self.env["BOOT_LDFLAGS"] = ldfl


@subpackage("libgccjit-devel")
def _(self):
    return self.default_devel()
