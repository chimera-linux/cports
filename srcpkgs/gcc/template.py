_majorver = "10"
_minorver = f"{_majorver}.2"
_patchver = f"{_minorver}.1"
_gmp_version = "6.2.0"
_mpfr_version = "4.1.0"
_mpc_version = "1.1.0"
_isl_version = "0.21"

pkgname = "gcc"
version = f"{_patchver}pre1"
wrksrc = f"gcc-{_patchver}_pre1"
revision = 3
make_cmd = "gmake"
short_desc = "GNU Compiler Collection"
maintainer = "Enno Boland <gottox@voidlinux.org>"
homepage = "http://gcc.gnu.org"
license = "GFDL-1.2-or-later, GPL-3.0-or-later, LGPL-2.1-or-later"

from cbuild import sites, cpu

distfiles = [
    f"https://dev.alpinelinux.org/~nenolod/{wrksrc}.tar.xz",
    f"https://gmplib.org/download/gmp/gmp-{_gmp_version}.tar.xz",
    f"{sites.gnu}/mpfr/mpfr-{_mpfr_version}.tar.xz",
    f"{sites.gnu}/mpc/mpc-{_mpc_version}.tar.gz",
    f"http://isl.gforge.inria.fr/isl-{_isl_version}.tar.bz2",
]

checksum = [
    "772cfd5d30eb9cc5a996fec9ba8cdcb45d37df1c9b5770610103b814b732c590",
    "258e6cd51b3fbdfc185c716d55f82c08aff57df0c6fbd143cf6ed561267a1526",
    "0c98a3f1732ff6ca4ea690552079da9c597872d30e96ec28414ee23c95558a7f",
    "6985c538143c1208dcb1ac42cedad6ff52e267b47e5f970183a3e75125b43c2e",
    "d18ca11f8ad1a39ab6d03d3dcb3365ab416720fcb65b42d69f34f51bf0a0e859"
]

nopie = True
bootstrap = True

if not current.bootstrapping:
    hostmakedepends = ["gmake", "texinfo", "perl", "flex"]

makedepends = ["zlib-devel"]
depends = [
    "binutils",
    f"libgcc-devel-{version}_{revision}",
    f"libstdc++-devel-{version}_{revision}",
    "musl-devel",
]
checkdepends = ["dejagnu"]

_triplet = cpu.match_target(
    "x86_64*", "x86_64-linux-musl",
    "aarch64*", "aarch64-linux-musl",
    "ppc64le*", "powerpc64le-linux-musl",
    "ppc64*", "powerpc64-linux-musl"
)

if current.cross_build:
    hostmakedepends.append("cross-" + _triplet)

def post_extract(self):
    import shutil
    shutil.copytree(
        self.builddir / ("gmp-" + _gmp_version), self.abs_wrksrc / "gmp"
    )
    shutil.copytree(
        self.builddir / ("mpfr-" + _mpfr_version), self.abs_wrksrc / "mpfr"
    )
    shutil.copytree(
        self.builddir / ("mpc-" + _mpc_version), self.abs_wrksrc / "mpc"
    )
    shutil.copytree(
        self.builddir / ("isl-" + _isl_version), self.abs_wrksrc / "isl"
    )

def pre_configure(self):
    import os

    with open(self.abs_wrksrc / "gcc/Makefile.in") as ifile:
        with open(self.abs_wrksrc / "gcc/Makefile.in.new", "w") as ofile:
            for ln in ifile:
                ofile.write(ln.replace("./fixinc.sh", "-c true"))

    os.rename(
        self.abs_wrksrc / "gcc/Makefile.in.new",
        self.abs_wrksrc / "gcc/Makefile.in"
    )

def do_configure(self):
    cargs = [
        "--prefix=/usr",
        "--mandir=/usr/share/man",
        "--infodir=/usr/share/info",
        "--libexecdir=/usr/lib",
        "--libdir=/usr/lib",
        "--enable-languages=c,c++,lto",
        "--enable-shared",
        "--enable-lto",
        "--enable-plugins",
        "--enable-linker-build-id",
        "--enable-threads=posix",
        "--enable-__cxa_atexit",
        "--enable-default-pie",
        "--enable-default-ssp",
        "--enable-checking=release",
        "--disable-gnu-unique-object",
        "--disable-libsanitizer",
        "--disable-libstdcxx-pch",
        "--disable-sjlj-exceptions",
        "--disable-target-libiberty",
        "--disable-multilib",
        "--disable-symvers",
        "--disable-werror",
        "--disable-nls",
        "--with-isl",
        "--with-system-zlib",
        "--with-linker-hash-style=gnu",
        "libat_cv_have_ifunc=no"
    ]

    cargs += cpu.match_target(
        "ppc64le*", [
            "--with-abi=elfv2",
            "--disable-libquadmath",
            "--disable-decimal-float",
            "--disable-vtable-verify",
            "--enable-targets=powerpcle-linux",
            "--enable-secureplt",
        ],
        "*", []
    )

    if not self.cross_build:
        cargs.append("--build=" + _triplet)

        if self.bootstrapping:
            from cbuild.core import paths
            self.env["LD_LIBRARY_PATH"] = str(paths.masterdir() / "usr/lib")
    else:
        self.env["CC_FOR_TARGET"] = self.tools["CC"]
        self.env["GCC_FOR_TARGET"] = self.tools["CC"]
        self.env["CXX_FOR_TARGET"] = self.tools["CXX"]

        cargs.append("--host=" + self.cross_triplet)
        cargs.append("--with-build-sysroot=" + self.cross_base)

    # gcc will figure this out by itself
    self.CFLAGS = [x for x in self.CFLAGS if x != "-fno-PIE"]
    self.CXXFLAGS = [x for x in self.CXXFLAGS if x != "-fno-PIE"]
    self.LDFLAGS = [x for x in self.CFLAGS if x != "-no-pie"]

    import os
    os.makedirs(self.abs_wrksrc / "build", exist_ok = True)
    self.do(self.chroot_wrksrc / "configure", cargs, wrksrc = "build")

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self, wrksrc = "build")

def do_build(self):
    self.make.build()

def do_install(self):
    self.install_dir("usr/lib")
    self.install_link("lib", "usr/lib" + str(cpu.target_wordsize()))

    self.make.install()

    self.unlink("usr/lib" + str(cpu.target_wordsize()))

    import shutil

    # make version a symlink of major versions to make
    # all versions from the same series work automagically
    shutil.move(
        self.destdir / "usr/lib/gcc" / _triplet / _patchver,
        self.destdir / "usr/lib/gcc" / _triplet / _minorver,
    )
    self.install_link(
        _minorver, f"usr/lib/gcc/{_triplet}/{_patchver}"
    )

    # ditto for c++
    shutil.move(
        self.destdir / "usr/include/c++" / _patchver,
        self.destdir / "usr/include/c++" / _minorver,
    )
    self.install_link(_minorver, f"usr/include/c++/{_patchver}")

    # cc symlink
    self.install_link("gcc", "usr/bin/cc")
    # rpcgen wants /lib/cpp, make a symlink
    self.install_link("../bin/cpp", "usr/lib/cpp")

    # lto plugin symlink
    self.install_dir("usr/lib/bfd-plugins")
    self.install_link(
        f"../gcc/{_triplet}/{_patchver}/liblto_plugin.so",
        "usr/lib/bfd-plugins/liblto_plugin.so"
    )

    # remove "fixed" header
    # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=91085
    self.unlink(
        f"usr/lib/gcc/{_triplet}/{_minorver}/include-fixed/bits/statx.h",
        missing_ok = True
    )

    # remove libffi stuff
    for f in (self.destdir / "usr/lib").glob("libffi*"):
        f.unlink()
    for f in (self.destdir / "usr/share/man/man3").glob("ffi*"):
        f.unlink()

    # remove all python scripts in libdir
    for f in (self.destdir / "usr/lib").rglob("*.py"):
        f.unlink()

    # remove more python stuff
    p = self.destdir / "usr/share" / ("gcc-" + _patchver) / "python"
    if p.is_dir():
        shutil.rmtree(p)

    # install c89 and c99 wrappers
    for f in ["c89", "c99"]:
        self.install_bin(self.files_path / (f + ".sh"))
        shutil.move(
            self.destdir / "usr/bin" / (f + ".sh"),
            self.destdir / "usr/bin" / f
        )
        self.install_man(self.files_path / (f + ".1"))

@subpackage("libgcc")
def _libgcc(self):
    self.short_desc = short_desc + " - GCC library"
    self.noverifyrdeps = True

    def install():
        self.take("usr/lib/libgcc_s.so*")
        self.install_license("COPYING.RUNTIME")

    return install

@subpackage("libgcc-devel")
def _libgcc_devel(self):
    self.depends = [f"libgcc-{version}_{revision}"]
    self.short_desc = short_desc + " - GCC library - development files"

    def install():
        self.take(f"usr/lib/gcc/{_triplet}/{_minorver}/*.o")
        self.take(f"usr/lib/gcc/{_triplet}/{_minorver}/*.a")

    return install

@subpackage("libstdc++-devel")
def _libstdc_devel(self):
    self.depends = [f"libstdc++>={_minorver}"]
    self.short_desc = short_desc + " - Standard C++ Library - development files"

    def install():
        self.take("usr/lib/libstdc++*.a")
        self.take("usr/lib/libsupc++.a")
        self.take("usr/include/c++")

    return install

@subpackage("libstdc++")
def _libstdc(self):
    self.short_desc = short_desc + " - Standard C++ Library"

    def install():
        self.take("usr/lib/libstdc++.so*")
        self.install_license("COPYING.RUNTIME")

    return install
