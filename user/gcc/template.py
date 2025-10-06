# rebuild on major clang version updates
pkgname = "gcc"
_clangver = "20"
pkgver = "15.2.0"
_bver = pkgver
_mnver = _bver[0 : _bver.rfind(".")]
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
    "--with-matchpd-partitions=32",
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
    "--with-system-zstd",
    "--with-linker-hash-style=gnu",
    f"--with-gxx-include-dir=/usr/include/c++/{_bver}",
    "--with-gxx-libcxx-include-dir=/usr/include/c++/v1",
    "libat_cv_have_ifunc=no",
]
configure_gen = []
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "bison",
    "flex",
    "gawk",
    "perl",
    "texinfo",
]
makedepends = [
    "gmp-devel",
    "isl-devel",
    "libcxx-devel-static",
    "libucontext-devel",
    "libunwind-devel-static",
    "mpc-devel",
    "mpfr-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = [
    f"binutils-{self.profile().arch}",
    f"clang-rt-devel~{_clangver}",
    f"libcxx-devel~{_clangver}",
]
pkgdesc = "GNU Compiler Collection"
license = "GPL-3.0-or-later"
url = "https://gcc.gnu.org"
source = f"$(GNU_SITE)/gcc/gcc-{pkgver}/gcc-{pkgver}.tar.xz"
sha256 = "438fd996826b0c82485a29da03a72d71d6e3541a83ec702df4271f6fe025d24e"
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

# not all archs have gcc-bootstrap and on some using the regular host
# clang to bootstrap is fine, but where we can bootstrap with gcc, do
# so in order to avoid trouble
_use_bootstrap = False

match self.profile().arch:
    case (
        "aarch64" | "armv7" | "ppc64le" | "ppc64" | "ppc" | "riscv64" | "x86_64"
    ):
        _use_bootstrap = True
        hostmakedepends += ["gcc-bootstrap"]

match self.profile().arch:
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

match self.profile().arch:
    case "ppc" | "x86":
        makedepends += ["musl-libssp-static"]
        depends += ["musl-libssp-static"]
        configure_args += ["--enable-autolink-libssp"]


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
    # bypass clang
    if _use_bootstrap:
        self.env["CC"] = (
            "/usr/lib/gcc-bootstrap/bin/gcc -I/usr/include -L/usr/lib"
        )
        self.env["CXX"] = (
            "/usr/lib/gcc-bootstrap/bin/g++ -I/usr/include -L/usr/lib"
        )


def post_install(self):
    # version symlink
    self.rename(f"usr/lib/gcc/{_trip}/{_bver}", f"{_mnver}")
    # link the runtime and nuke libgcc
    self.install_link(
        f"usr/lib/gcc/{_trip}/{_mnver}/libclang_rt.builtins.a",
        f"../../../clang/{_clangver}/lib/{_trip}/libclang_rt.builtins.a",
    )
    self.uninstall(f"usr/lib/gcc/{_trip}/{_mnver}/libgcc*.a", glob=True)
    # nuke libstdc++; this build is not compatible with chimera
    self.uninstall("usr/include/c++")
    self.uninstall("usr/lib/libstdc++*", glob=True)
    self.uninstall("usr/lib/libsupc++.*", glob=True)
    self.uninstall("usr/share/gcc-*/python/libstdcxx", glob=True)
    # other stuff we don't want
    self.uninstall("usr/lib/libatomic.*", glob=True)
    self.uninstall("usr/lib/libgcc_s.*", glob=True)
    # provided by clang
    self.uninstall("usr/bin/c++")
    self.uninstall(f"usr/bin/{_trip}-c++")
    # hardlinks
    for f in ["g++", "gcc", "gcc-ar", "gcc-nm", "gcc-ranlib", "gfortran"]:
        self.uninstall(f"usr/bin/{_trip}-{f}")
        self.install_link(f"usr/bin/{_trip}-{f}", f)
    self.uninstall(f"usr/bin/{_trip}-gcc")
    self.uninstall(f"usr/bin/{_trip}-gcc-{_bver}")
    self.install_link(f"usr/bin/{_trip}-gcc-{_bver}", "gcc")
    self.install_link(f"usr/bin/{_trip}-gcc", f"{_trip}-gcc-{_bver}")
    # lto plugin symlink
    self.install_dir("usr/lib/bfd-plugins")
    self.install_link(
        "usr/lib/bfd-plugins/liblto_plugin.so",
        f"../gcc/{_trip}/{_bver}/liblto_plugin.so",
    )
    self.install_link(f"usr/lib/gcc/{_trip}/{_bver}", _mnver)


@subpackage("gcc-fortran")
def _(self):
    self.subdesc = "Fortran frontend"
    self.depends = [self.parent]
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
def _(self):
    self.subdesc = "Objective-C"
    self.depends = [self.parent]
    self.nopie_files = [
        f"usr/lib/gcc/{_trip}/{_mnver}/cc1obj",
    ]
    return [
        "usr/lib/libobjc.a",
        "usr/lib/libobjc.so",
        f"usr/lib/gcc/{_trip}/{_mnver}/include/objc",
        f"usr/lib/gcc/{_trip}/{_mnver}/cc1obj",
    ]


@subpackage("gcc-fortran-libs")
def _(self):
    self.subdesc = "Fortran runtime library"
    return ["usr/lib/libgfortran.so.*"]


@subpackage("gcc-objc-libs")
def _(self):
    self.subdesc = "Objective-C runtime library"
    return ["usr/lib/libobjc.so.*"]


@subpackage("gcc-gomp-devel")
def _(self):
    self.subdesc = "OpenMP develpment files"
    return [
        f"usr/lib/gcc/{_trip}/{_mnver}/include/omp.h",
        "usr/lib/libgomp.so",
        "usr/lib/libgomp.a",
        "usr/lib/libgomp.spec",
        "usr/share/info/libgomp.info",
    ]


@subpackage("gcc-gomp-libs")
def _(self):
    self.subdesc = "OpenMP runtime"
    return ["usr/lib/libgomp.so.*"]


@subpackage("gcc-itm-devel")
def _(self):
    self.subdesc = "transactional memory lib development files"
    return [
        "usr/lib/libitm.so",
        "usr/lib/libitm.a",
        "usr/lib/libitm.spec",
        "usr/share/info/libitm.info",
    ]


@subpackage("gcc-itm-libs")
def _(self):
    self.subdesc = "transactional memory library"
    return ["usr/lib/libitm.so.*"]
