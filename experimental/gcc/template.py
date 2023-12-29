# rebuild on major clang version updates
pkgname = "gcc"
_clangver = "17"
_mver = "13"
_mnver = f"{_mver}.2"
_bver = f"{_mnver}.1"
_datever = "20231014"
pkgver = f"{_bver}_git{_datever}"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libdir=/usr/lib",
    "--libexecdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--disable-cet",
    "--disable-fixed-point",
    "--disable-nls",
    "--disable-libsanitizer",
    "--disable-libssp",
    "--disable-libstdcxx-pch",
    # we can't enable this yet as the compiler-rt builtins don't have quad yet
    # TODO for llvm 18 i guess? could work around it probably
    "--disable-libquadmath",
    "--disable-libquadmath-support",
    "--disable-multilib",
    "--disable-symvers",
    "--disable-target-libiberty",
    "--disable-vtable-verify",
    "--disable-werror",
    "--enable-checking=release",
    "--enable-autolink-libatomic",
    "--enable-__cxa_atexit",
    "--enable-default-pie",
    "--enable-default-ssp",
    # more languages later
    "--enable-languages=c,c++,objc,fortran",
    "--enable-linker-build-id",
    "--enable-plugins",
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
    "--with-linker-hash-style=gnu",
    f"--with-gxx-include-dir=/usr/include/c++/{_bver}",
    "--with-gxx-libcxx-include-dir=/usr/include/c++/v1",
    "libat_cv_have_ifunc=no",
]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    f"binutils-{self.profile().arch}",
    "bison",
    "flex",
    "gawk",
    "perl",
    "texinfo",
]
makedepends = [
    "isl-devel",
    "gmp-devel",
    "libcxx-devel-static",
    "libucontext-devel",
    "libunwind-devel-static",
    "mpfr-devel",
    "mpc-devel",
    "zlib-devel",
]
depends = [
    f"binutils-{self.profile().arch}",
    f"clang-rt-devel~{_clangver}",
    f"libcxx-devel~{_clangver}",
]
pkgdesc = "GNU Compiler Collection"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"https://dev.alpinelinux.org/archive/gcc/{_mver}-{_datever}/gcc-{_mver}-{_datever}.tar.xz"
sha256 = "40bf42e54cefefa4a8f35c48e0f290c9ef8118eee9a72800296a0e620dfb0240"
hardening = ["!int", "!format", "!var-init"]
# no tests to run
options = ["!check", "!lto", "!relr", "!cross", "!scanshlibs"]

_trip = self.profile().triplet
# we cannot use clang, gcc expects binutils
tools = {"AS": "as", "LD": "ld.bfd", "OBJDUMP": "gobjdump"}
# give the build the builtins library in all cases that use LDFLAGS
tool_flags = {"LDFLAGS": [f"-L/usr/lib/clang/{_clangver}/lib/{_trip}"]}
# sigh
nopie_files = [
    "usr/bin/*",
    f"usr/lib/gcc/{_trip}/{_mnver}/*",
    f"usr/lib/gcc/{_trip}/{_mnver}/plugin/*",
]
# skip those
broken_symlinks = [
    f"usr/lib/gcc/{_trip}/{_mnver}/libclang_rt.builtins.a",
]

match self.profile().arch:
    case "aarch64":
        configure_args += [
            "--with-arch=armv8-a",
            "--with-abi=lp64",
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
    case "riscv64":
        configure_args += [
            "--with-arch=rv64gc",
            "--with-abi=lp64d",
        ]


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


def post_install(self):
    # version symlink
    self.mv(
        self.destdir / f"usr/lib/gcc/{_trip}/{_bver}",
        self.destdir / f"usr/lib/gcc/{_trip}/{_mnver}",
    )
    # link the runtime and nuke libgcc
    self.install_link(
        f"../../../clang/{_clangver}/lib/{_trip}/libclang_rt.builtins.a",
        f"usr/lib/gcc/{_trip}/{_mnver}/libclang_rt.builtins.a",
    )
    self.rm(self.destdir / f"usr/lib/gcc/{_trip}/{_mnver}/libgcc*.a", glob=True)
    # nuke libstdc++; this build is not compatible with chimera
    self.rm(self.destdir / "usr/include/c++", recursive=True)
    self.rm(self.destdir / "usr/lib/libstdc++*", glob=True)
    self.rm(self.destdir / "usr/lib/libsupc++.*", glob=True)
    self.rm(
        self.destdir / "usr/share/gcc-*/python/libstdcxx",
        recursive=True,
        glob=True,
    )
    # other stuff we don't want
    self.rm(self.destdir / "usr/lib/libatomic.*", glob=True)
    self.rm(self.destdir / "usr/lib/libgcc_s.*", glob=True)
    # provided by clang
    self.rm(self.destdir / "usr/bin/c++")
    self.rm(self.destdir / f"usr/bin/{_trip}-c++")
    # hardlinks
    for f in ["g++", "gcc", "gcc-ar", "gcc-nm", "gcc-ranlib", "gfortran"]:
        self.rm(self.destdir / f"usr/bin/{_trip}-{f}")
        self.install_link(f, f"usr/bin/{_trip}-{f}")
    self.rm(self.destdir / f"usr/bin/{_trip}-gcc")
    self.rm(self.destdir / f"usr/bin/{_trip}-gcc-{_bver}")
    self.install_link("gcc", f"usr/bin/{_trip}-gcc-{_bver}")
    self.install_link(f"{_trip}-gcc-{_bver}", f"usr/bin/{_trip}-gcc")
    # lto plugin symlink
    self.install_dir("usr/lib/bfd-plugins")
    self.install_link(
        f"../gcc/{_trip}/{_bver}/liblto_plugin.so",
        "usr/lib/bfd-plugins/liblto_plugin.so",
    )
    self.install_link(_mnver, f"usr/lib/gcc/{_trip}/{_bver}")


@subpackage("gcc-fortran")
def _fortran(self):
    self.pkgdesc = f"{pkgdesc} (Fortran frontend)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.nopie_files = [
        "usr/bin/gfortran",
        f"usr/lib/gcc/{_trip}/{_mnver}/f951",
    ]
    return [
        "usr/bin/gfortran",
        "usr/bin/*-gfortran",
        "usr/lib/libgfortran.spec",
        "usr/lib/libgfortran.a",
        "usr/lib/libgfortran.so",
        f"usr/lib/gcc/{_trip}/{_mnver}/f951",
        f"usr/lib/gcc/{_trip}/{_mnver}/libcaf_single.a",
        f"usr/lib/gcc/{_trip}/{_mnver}/finclude",
        "usr/share/info/gfortran.info",
        "usr/share/man/man1/gfortran.1",
    ]


@subpackage("gcc-objc")
def _objc(self):
    self.pkgdesc = f"{pkgdesc} (Objective-C)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.nopie_files = [
        f"usr/lib/gcc/{_trip}/{_mnver}/cc1obj",
    ]
    return [
        "usr/lib/libobjc.a",
        "usr/lib/libobjc.so",
        f"usr/lib/gcc/{_trip}/{_mnver}/include/objc",
        f"usr/lib/gcc/{_trip}/{_mnver}/cc1obj",
    ]


@subpackage("libgfortran")
def _libfortran(self):
    self.pkgdesc = f"{pkgdesc} (Fortran runtime library)"
    return ["usr/lib/libgfortran.so.*"]


@subpackage("libobjc")
def _libobjc(self):
    self.pkgdesc = f"{pkgdesc} (Objective-C runtime library)"
    return ["usr/lib/libobjc.so.*"]


@subpackage("libgomp-devel")
def _gompdev(self):
    self.pkgdesc = f"{pkgdesc} (OpenMP develpment files)"
    return [
        f"usr/lib/gcc/{_trip}/{_mnver}/include/omp.h",
        "usr/lib/libgomp.so",
        "usr/lib/libgomp.a",
        "usr/lib/libgomp.spec",
        "usr/share/info/libgomp.info",
    ]


@subpackage("libgomp")
def _gomp(self):
    self.pkgdesc = f"{pkgdesc} (OpenMP runtime)"
    return ["usr/lib/libgomp.so.*"]


@subpackage("libitm-devel")
def _itmdev(self):
    self.pkgdesc = f"{pkgdesc} (transactional memory lib development files)"
    return [
        "usr/lib/libitm.so",
        "usr/lib/libitm.a",
        "usr/lib/libitm.spec",
        "usr/share/info/libitm.info",
    ]


@subpackage("libitm")
def _itm(self):
    self.pkgdesc = f"{pkgdesc} (transactional memory library)"
    return ["usr/lib/libitm.so.*"]
