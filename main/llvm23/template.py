pkgname = "llvm23"
pkgver = "23.1.6"
_majver = pkgver[0:2]
pkgrel = 1
build_style = "cmake"
_pfx = f"usr/lib/llvm{_majver}"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    f"-DCMAKE_INSTALL_PREFIX=/{_pfx}",
    # use rpath so the installed tools always use their own libs
    f"-DCMAKE_INSTALL_RPATH=/{_pfx}/lib",
    "-DENABLE_LINKER_BUILD_ID=ON",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=ON",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # avoid execinfo
    "-DCOMPILER_RT_BUILD_GWP_ASAN=OFF",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=ON",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=OFF",
    "-DLIBCXX_HAS_MUSL_LIBC=ON",
    "-DLIBCXX_HARDENING_MODE=fast",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=ON",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=OFF",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    "-DLLVM_INSTALL_BINUTILS_SYMLINKS=ON",
    "-DLLVM_INSTALL_UTILS=ON",
    "-DLLVM_BUILD_LLVM_DYLIB=ON",
    "-DLLVM_LINK_LLVM_DYLIB=ON",
    "-DLLVM_ENABLE_RTTI=ON",
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
    "-DCLANG_DEFAULT_RTLIB=compiler-rt",
    "-DCLANG_DEFAULT_UNWINDLIB=libunwind",
    "-DCLANG_DEFAULT_CXX_STDLIB=libc++",
    "-DCLANG_CONFIG_FILE_SYSTEM_DIR=/etc/clang",
    "-DLLVM_ENABLE_LIBXML2=OFF",
    "-DLLVM_ENABLE_LIBCXX=ON",
    "-DLIBUNWIND_ENABLE_ASSERTIONS=OFF",
    "-DLIBUNWIND_USE_COMPILER_RT=ON",
    "-DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF",
]
cmake_dir = "llvm"
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
    "python",
    "zlib-ng-compat-devel",
]
makedepends = ["zlib-ng-compat-devel", "libatomic-chimera-devel"]
depends = [
    self.with_pkgver(f"llvm{_majver}-libs"),
    self.with_pkgver(f"llvm{_majver}-binutils"),
]
pkgdesc = "Low Level Virtual Machine - 23.x"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "d3b86ab29cfb4445a6652e5c2642ccc75e04e38084dde3701d323320f35a31da"
# reduce size of debug symbols
debug_level = 1
tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
    "LDFLAGS": [],
}
# disable ubsan integer checks, it breaks aarch64/riscv64/ppc64 targets
# when lto-linking lld with ubsan'd clang/lld, it causes
# that to crash in 'AArch64 Instruction Selection'
# (on ppc64le, 'PowerPC Instruction Selection' e.g.
# when building graphviz)
# while on riscv it prevents rust from building
hardening = ["!int"]
# lto does not kick in until stage 2
# tests are not enabled
# runtimes build may invoke built clang during install, which has
# rpath and fakeroot effectively overrides rpath, so disable that
options = ["bootstrap", "!ci", "!check", "!installroot"]

_enabled_projects = ["clang", "clang-tools-extra", "lld"]
_enabled_runtimes = ["compiler-rt", "libcxx", "libcxxabi", "libunwind"]

if self.stage > 0:
    configure_args += ["-DLLVM_ENABLE_FFI=ON"]
    hostmakedepends += ["libffi8-devel"]
    makedepends += [
        "python-devel",
        "libedit-devel",
        "libffi8-devel",
        "zstd-devel",
        "linux-headers",
    ]
    # enable LTO except on riscv where it's broken
    # also use llvm-bootstrap
    if not self.profile.cross:
        hostmakedepends += ["llvm-bootstrap"]
        # set all the stuff that matters
        configure_args += [
            "-DCMAKE_AR=/usr/lib/llvm-bootstrap/bin/llvm-ar",
            "-DCMAKE_NM=/usr/lib/llvm-bootstrap/bin/llvm-nm",
            "-DCMAKE_RANLIB=/usr/lib/llvm-bootstrap/bin/llvm-ranlib",
            "-DLLVM_USE_LINKER=/usr/lib/llvm-bootstrap/bin/ld.lld",
        ]
        # not fun but stuff used during build may be using symbols from
        # a newer version of libcxx so we need to point it to bootstrap
        tool_flags["LDFLAGS"] += [
            "--ld-path=/usr/lib/llvm-bootstrap/bin/ld.lld",
            "-L/usr/lib/llvm-bootstrap/lib",
        ]
        # this so it resolves at runtime too (e.g. -tblgen runs)
        make_build_env = {"LD_LIBRARY_PATH": "/usr/lib/llvm-bootstrap/lib"}
    else:
        configure_args += ["-DLLVM_ENABLE_LLD=ON"]
        # don't build flang/mlir for stage 1 to save time
        if self.stage >= 2:
            hostmakedepends += [
                f"llvm{_majver}",
                f"llvm{_majver}-clang-tools-extra",
                f"llvm{_majver}-mlir",
            ]
else:
    configure_args += [
        "-DLLVM_ENABLE_LLD=ON",
        "-DLLVM_ENABLE_LIBEDIT=OFF",
        "-DLLVM_ENABLE_LIBPFM=OFF",
        # for stage 0 bootstrap, avoid all the optional runtime
        "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
        "-DCOMPILER_RT_BUILD_XRAY=OFF",
        "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
        "-DCOMPILER_RT_BUILD_PROFILE=OFF",
        "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
        "-DCOMPILER_RT_BUILD_CTX_PROFILE=OFF",
    ]

# from stage 2 only, pointless to build before
_enable_mlir = self.stage >= 2 and not self.profile.cross
_enable_flang = _enable_mlir and self.profile.wordsize == 64

if _enable_mlir:
    _enabled_projects += ["mlir"]

if _enable_flang:
    _enabled_projects += ["flang"]

match self.profile.arch:
    case "x86_64":
        _arch = "X86"
    case "aarch64":
        _arch = "AArch64"
    case "ppc64le" | "ppc64" | "ppc":
        _arch = "PowerPC"
    case "riscv64":
        _arch = "RISCV64"
    case "armhf" | "armv7":
        _arch = "ARM"
    case "loongarch64" | "loongarch32":
        _arch = "LoongArch"
    case _:
        broken = f"Unknown CPU architecture: {self.profile.arch}"

configure_args += [f"-DLLVM_ENABLE_PROJECTS={';'.join(_enabled_projects)}"]
configure_args += [f"-DLLVM_ENABLE_RUNTIMES={';'.join(_enabled_runtimes)}"]


def init_configure(self):
    if self.has_lto():
        self.configure_args += ["-DLLVM_ENABLE_LTO=Thin"]

    if not self.profile.cross:
        if self.stage > 0:
            self.configure_args += [
                f"-DCMAKE_C_COMPILER={self.chroot_cwd / 'boot-clang'}",
                f"-DCMAKE_CXX_COMPILER={self.chroot_cwd / 'boot-clang++'}",
            ]
        return

    # grab these from the host
    self.configure_args += [
        f"-DLLVM_NATIVE_TOOL_DIR=/{_pfx}/bin",
        f"-DLLVM_CONFIG_PATH=/{_pfx}/bin/llvm-config",
        f"-DLLVM_HEADERS_TABLEGEN=/{_pfx}/bin/llvm-tblgen",
        f"-DLLVM_TABLEGEN=/{_pfx}/bin/llvm-tblgen",
        f"-DLLVM_HEADERS_TABLEGEN=/{_pfx}/bin/llvm-tblgen",
        f"-DCLANG_TABLEGEN=/{_pfx}/bin/clang-tblgen",
        f"-DCLANG_TIDY_CONFUSABLE_CHARS_GEN=/{_pfx}/bin/clang-tidy-confusable-chars-gen",
    ]


def configure(self):
    from cbuild.util import cmake

    # when bootstrapping, this will check the actual profile
    with self.use_profile(self.profile.arch) as pf:
        trip = pf.triplet

    for f in ["clang", "clang++"]:
        outp = self.cwd / f"boot-{f}"
        if not self.use_ccache:
            outp.symlink_to(f"/usr/lib/llvm-bootstrap/bin/{f}")
            continue
        with open(outp, "w") as outf:
            outf.write(f"""#!/bin/sh
exec /usr/bin/ccache /usr/lib/llvm-bootstrap/bin/{f} "$@"
""")
        outp.chmod(0o755)

    cmake.configure(
        self,
        "build",
        self.cmake_dir,
        [
            *self.configure_args,
            "-DLLVM_TARGET_ARCH=" + _arch,
            "-DLLVM_HOST_TRIPLE=" + trip,
            "-DLLVM_DEFAULT_TARGET_TRIPLE=" + trip,
        ],
    )


def post_install(self):
    from cbuild.util import python

    # our toolchain defaults
    self.install_link(f"{_pfx}/bin/cc", "clang")
    self.install_link(f"{_pfx}/bin/c++", "clang++")
    self.install_file(self.files_path / "c99", f"{_pfx}/bin", mode=0o755)
    self.install_file(self.files_path / "c89", f"{_pfx}/bin", mode=0o755)

    if not (self.destdir / f"{_pfx}/bin/ld").is_symlink():
        self.install_link(f"{_pfx}/bin/ld", "ld.lld")

    # make stage0 bootstrap profile happy
    with self.use_profile(self.profile.arch) as pf:
        trip = pf.triplet

    # arch-prefixed symlinks for cross consistency (no config file)
    self.install_link(f"{_pfx}/bin/{trip}-clang", "clang")
    self.install_link(f"{_pfx}/bin/{trip}-clang++", "clang++")
    self.install_link(f"{_pfx}/bin/{trip}-clang-cpp", "clang-cpp")
    self.install_link(f"{_pfx}/bin/{trip}-cc", "cc")
    self.install_link(f"{_pfx}/bin/{trip}-c++", "c++")
    self.install_link(f"{_pfx}/bin/{trip}-ld", "ld")
    self.install_link(f"{_pfx}/bin/{trip}-ld.lld", "ld.lld")

    self.install_license("LICENSE.TXT")

    # we don't want debuginfod symlinks, these may be provided by actual
    # debuginfod from elfutils (and there is no need to alias them)
    self.uninstall(f"{_pfx}/bin/debuginfod")
    self.uninstall(f"{_pfx}/bin/debuginfod-find")

    # python bytecode cache
    if self.stage > 0:
        python.precompile(self, f"{_pfx}/share/scan-view")

    # extra cross bins, not super useful outside of that but harmless
    self.install_file(
        "build/bin/clang-tidy-confusable-chars-gen",
        f"{_pfx}/bin",
        mode=0o755,
    )

    # make global links for all bins
    self.install_dir("usr/bin")
    for lbin in sorted((self.destdir / f"{_pfx}/bin").iterdir()):
        if lbin.name.endswith(f"-{_majver}"):
            # skip internally versioned bins
            continue
        self.install_link(
            f"usr/bin/{lbin.name}-{_majver}",
            f"../lib/llvm{_majver}/bin/{lbin.name}",
        )
        self.install_link(f"usr/bin/{lbin.name}", f"{lbin.name}-{_majver}")

    # ccache links
    cpfx = "usr/lib/ccache/bin"
    self.install_dir(cpfx)
    for cf in ["clang", "clang++", "cc", "c++"]:
        self.install_link(f"{cpfx}/{cf}", "../../../bin/ccache")
        self.install_link(f"{cpfx}/{cf}-{_majver}", "../../../bin/ccache")
        self.install_link(f"{cpfx}/{trip}-{cf}", "../../../bin/ccache")
        self.install_link(
            f"{cpfx}/{trip}-{cf}-{_majver}", "../../../bin/ccache"
        )

    # move runtimes into default prefix as only one link copy is allowed
    for lname in [
        "libc++abi.a",
        "libc++abi.so",
        "libc++abi.so.1",
        "libc++abi.so.1.0",
        "libc++.a",
        "libc++.so",
        "libc++.so.1",
        "libc++.so.1.0",
        "libc++experimental.a",
        "libunwind.a",
        "libunwind.so",
        "libunwind.so.1",
        "libunwind.so.1.0",
    ]:
        self.rename(f"{_pfx}/lib/{lname}", f"usr/lib/{lname}", relative=False)

    # libunwind headers are global too, we only allow a single copy (latest)
    self.rename(f"{_pfx}/include/mach-o", "usr/include/mach-o", relative=False)
    for unw in (self.destdir / f"{_pfx}/include").glob("*unwind*"):
        self.rename(
            f"{_pfx}/include/{unw.name}",
            f"usr/include/{unw.name}",
            relative=False,
        )


def _verbin(self, binf):
    rself = self.rparent
    globl = list((rself.destdir / f"{_pfx}/bin").glob(binf))
    if not globl:
        rself.error(f"no matches for '{binf}'")
    for lbin in globl:
        self.take(f"{_pfx}/bin/{lbin.name}")
        if lbin.name.endswith(f"-{_majver}"):
            # skip internally versioned bins
            continue
        # global symlink
        self.take(f"usr/bin/{lbin.name}-{_majver}")


def _defbin(self, binf):
    rself = self.rparent
    globl = list((rself.destdir / "usr/bin").glob(binf))
    if not globl:
        rself.error(f"no matches for '{binf}'")
    for lbin in globl:
        if lbin.name.endswith(f"-{_majver}"):
            # skip internally versioned bins
            continue
        self.take(f"usr/bin/{lbin.name}")


def _verlib(self, libf):
    rself = self.rparent
    globl = list((rself.destdir / f"{_pfx}/lib").glob(libf))
    if not globl:
        rself.error(f"no matches for '{libf}'")
    for llib in globl:
        self.take(f"{_pfx}/lib/{llib.name}")
        # global symlink
        self.make_link(
            f"usr/lib/{llib.name}", f"../lib/llvm{_majver}/lib/{llib.name}"
        )


def _vergen(self, libf):
    self.take(f"{_pfx}/{libf}")


_bins = {
    "clang-tools-extra": [
        "clang-apply-replacements",
        "clang-query",
        "clang-tidy",
        "clang-tidy-confusable-chars-gen",
        "diagtool",
        "find-all-symbols",
        "hmaptool",
        "modularize",
        "pp-trace",
        "run-clang-tidy",
        "sancov",
    ],
    "binutils": [
        "addr2line",
        "ar",
        "c++filt",
        "dlltool",
        "dwp",
        "llvm-addr2line",
        "llvm-ar",
        "llvm-bitcode-strip",
        "llvm-cxxfilt",
        "llvm-dlltool",
        "llvm-dwp",
        "llvm-install-name-tool",
        "llvm-lib",
        "llvm-nm",
        "llvm-objcopy",
        "llvm-objdump",
        "llvm-ranlib",
        "llvm-rc",
        "llvm-readelf",
        "llvm-readobj",
        "llvm-size",
        "llvm-strings",
        "llvm-strip",
        "llvm-symbolizer",
        "nm",
        "objcopy",
        "objdump",
        "ranlib",
        "readelf",
        "size",
        "strings",
        "strip",
        "windres",
    ],
    "clang": [
        "*clang*",
        "*-cc",
        "*-c++",
        "c-index-test",
        "cc",
        "c89",
        "c99",
        "c++",
    ],
    "clang-analyzer": ["analyze-build", "intercept-build", "scan-*"],
    "flang": ["bbc", "f18*", "fir*", "flang*", "tco"],
    "mlir": ["mlir*"],
    "lld": ["*-ld*", "ld", "lld*", "ld.lld*", "ld64.lld*"],
}


def _verbins(self, binl, default):
    for b in _bins[binl]:
        if default:
            _defbin(self, b)
        else:
            _verbin(self, b)


@split("clang-tools-extra-static")
def _(self):
    self.subdesc = "extra Clang tools static libraries"
    self.depends = []
    self.install_if = []

    def install():
        _vergen(self, "lib/libclangApplyReplacements*")
        _vergen(self, "lib/libclangQuery*")
        _vergen(self, "lib/libclangTidy*")

    return install


@split("clang-tools-extra")
def _(self):
    self.subdesc = "extra Clang tools"
    self.depends = [
        self.with_pkgver(f"llvm{_majver}-clang"),
        self.with_pkgver(f"llvm{_majver}-clang-tools-extra-static"),
    ]

    def install():
        _verbins(self, "clang-tools-extra", False)
        _vergen(self, "include/clang-tidy")
        _vergen(self, "share/clang/*tidy*")

    return install


@split("clang-tools-extra-default")
def _(self):
    self.subdesc = "extra Clang tools default links"

    return lambda: _verbins(self, "clang-tools-extra", True)


@split("binutils")
def _(self):
    self.subdesc = "binary manipulation tools"

    return lambda: _verbins(self, "binutils", False)


@split("binutils-default")
def _(self):
    self.subdesc = "binary manipulation tools default links"
    self.replaces = ["elftoolchain<0.7.1_svn20230501"]

    return lambda: _verbins(self, "binutils", True)


@split("clang")
def _(self):
    self.subdesc = "C language family frontend"
    self.depends = [
        self.with_pkgver(f"llvm{_majver}-runtimes-devel"),
        self.with_pkgver(f"llvm{_majver}-clang-rt-devel"),
        self.with_pkgver(f"llvm{_majver}-lld"),
        self.with_pkgver(f"llvm{_majver}-binutils"),
        "fortify-headers",
        "libatomic-chimera-devel",
        "musl-devel",
    ]
    self.broken_symlinks = ["usr/lib/ccache/bin/*"]

    def install():
        _verbins(self, "clang", False)
        _vergen(self, "lib/cmake/clang")
        _vergen(self, "share/clang")
        _vergen(self, "share/clang-doc")
        # versioned ccache links
        self.take(f"usr/lib/ccache/bin/*-{_majver}")

    return install


@split("clang-default")
def _(self):
    self.subdesc = "C language family frontend default links"
    self.replaces = ["ccache<4.14"]
    self.broken_symlinks = ["usr/lib/ccache/bin/*"]

    def install():
        _verbins(self, "clang", True)
        # versioned ccache links
        self.take("usr/lib/ccache/bin")

    return install


@split("clang-rt-devel")
def _(self):
    self.subdesc = "Clang runtime development files"
    self.options = ["ltostrip", "!splitstatic"]  # these are explicitly -fno-lto

    return lambda: _vergen(self, "lib/clang")


@split("clang-devel-static")
def _(self):
    self.subdesc = "Clang static libraries"
    self.depends = []
    self.install_if = []

    return lambda: _vergen(self, "lib/libclang*.a")


@split("clang-devel")
def _(self):
    self.subdesc = "Clang development files"
    # unfortunately cmake files reference the static libs and force their
    # installation onto the target system, nothing much we can do about that
    self.depends = [
        self.with_pkgver(f"llvm{_majver}-clang-rt-devel"),
        self.with_pkgver(f"llvm{_majver}-clang-devel-static"),
        self.with_pkgver(f"llvm{_majver}-clang-libs"),
        self.with_pkgver(f"llvm{_majver}-clang-cpp-libs"),
        self.with_pkgver(f"llvm{_majver}-runtimes-devel"),
    ]

    def install():
        _vergen(self, "include/clang")
        _vergen(self, "include/clang-c")
        _vergen(self, "lib/libclang*.so")

    return install


@split("clang-analyzer")
def _(self):
    self.subdesc = "source code analysis"
    self.depends = [self.with_pkgver(f"llvm{_majver}-clang")]
    if self.stage > 0:
        self.depends += ["perl", "python"]

    def install():
        _verbins(self, "clang-analyzer", False)
        _vergen(self, "lib/libear")
        _vergen(self, "lib/libscanbuild")
        _vergen(self, "lib/analyze-*")
        _vergen(self, "lib/*analyzer")
        _vergen(self, "lib/intercept-*")
        _vergen(self, "share/scan-*")
        _vergen(self, "share/man/man1/scan-build.1")

    return install


@split("clang-analyzer-default")
def _(self):
    self.subdesc = "source code analysis default links"

    return lambda: _verbins(self, "clang-analyzer", True)


@split("clang-libs")
def _(self):
    self.subdesc = "Clang runtime library"

    return lambda: _verlib(self, "libclang.so.*")


@split("clang-cpp-libs")
def _(self):
    self.subdesc = "Clang C++ runtime library"

    return lambda: _verlib(self, "libclang-cpp.so.*")


@split("flang", _enable_flang)
def _(self):
    self.subdesc = "Fortran frontend"
    self.depends = [
        self.with_pkgver(f"llvm{_majver}-clang"),
        self.with_pkgver(f"llvm{_majver}-flang-devel"),
    ]

    return lambda: _verbins(self, "flang", False)


@split("flang-default", _enable_flang)
def _(self):
    self.subdesc = "Fortran frontend default links"

    return lambda: _verbins(self, "flang", True)


@split("flang-devel-static", _enable_flang)
def _(self):
    self.subdesc = "Flang static libraries"
    self.depends = []
    self.install_if = []

    def install():
        _vergen(self, "lib/libFIR*.a")
        _vergen(self, "lib/libflang*.a")
        _vergen(self, "lib/libFortran*.a")
        _vergen(self, "lib/libHLFIR*.a")

    return install


@split("flang-devel", _enable_flang)
def _(self):
    self.subdesc = "Flang development files"
    self.depends = [self.with_pkgver(f"llvm{_majver}-flang-devel-static")]

    def install():
        _vergen(self, "include/flang")
        _vergen(self, "lib/cmake/flang")

    return install


@split("mlir", _enable_mlir)
def _(self):
    self.subdesc = "MLIR"

    return lambda: _verbins(self, "mlir", False)


@split("mlir-default", _enable_mlir)
def _(self):
    self.subdesc = "MLIR default links"

    return lambda: _verbins(self, "mlir", True)


@split("mlir-devel-static", _enable_mlir)
def _(self):
    self.subdesc = "MLIR static libraries"
    self.depends = []
    self.install_if = []

    return lambda: _vergen(self, "lib/libMLIR*.a")


@split("mlir-devel", _enable_mlir)
def _(self):
    self.subdesc = "MLIR development files"
    self.depends = [self.with_pkgver(f"llvm{_majver}-mlir-devel-static")]

    def install():
        _vergen(self, "include/mlir*")
        _vergen(self, "lib/libMLIR*.so")
        _vergen(self, "lib/libmlir*.so")
        _vergen(self, "lib/cmake/mlir")

    return install


@split("mlir-libs", _enable_mlir)
def _(self):
    self.subdesc = "MLIR runtime libraries"

    def install():
        _verlib(self, "libMLIR*.so.*")
        _verlib(self, "libmlir*.so.*")

    return install


@split("runtimes")
def _(self):
    self.subdesc = "runtimes"
    self.renames = [
        "libcxx",
        "libcxxabi",
        "libunwind",
    ]
    # prevent other things from depending on this by name
    self.options = ["looseshlibs"]

    return [
        "usr/lib/libc++*.so.*",
        "usr/lib/libunwind.so.*",
    ]


# we only allow one system copy of the runtimes (libunwind/libcxxabi/libcxx),
# with the exception of c++ stdlib headers which are specific to the toolchain
# (as newer stdlib may not work with older toolchain)
@split("runtimes-base-devel")
def _(self):
    self.subdesc = "runtimes base devel files"
    # don't resolve via symlink
    self.depends = [
        f"so:libc++abi.so.1!llvm{_majver}-runtimes",
        f"so:libc++.so.1!llvm{_majver}-runtimes",
        f"so:libunwind.so.1!llvm{_majver}-runtimes",
    ]
    self.options = ["!scanrundeps", "ltostrip", "!splitstatic"]
    self.provides = [self.with_pkgver("llvm-runtimes-devel-default")]

    return [
        "usr/include/*unwind*",
        "usr/include/mach-o",
        "usr/lib/libc++experimental.a",
        "usr/lib/libc++*.so",
        "usr/lib/libunwind.so",
    ]


# the same goes for static, the linked lib should be reasonably abi-stable
@split("runtimes-devel-static")
def _(self):
    self.subdesc = "static runtimes"
    # in global path and only one is installable
    self.provides = [self.with_pkgver("llvm-runtimes-devel-static-default")]
    self.options = ["ltostrip"]

    return [
        "usr/lib/libc++*.a",
        "usr/lib/libunwind.a",
    ]


@split("runtimes-devel")
def _(self):
    self.subdesc = "runtimes development files"
    self.depends += [
        f"virtual:llvm-runtimes-devel-default!llvm{_majver}-runtimes-base-devel"
    ]

    def install():
        _vergen(self, "lib/libc++.modules.json")
        _vergen(self, "include/c++")
        _vergen(self, "share/libc++")

    return install


@split("libs")
def _(self):
    def install():
        _verlib(self, "libLLVM.so.*")
        _verlib(self, f"libLLVM-{_majver}*.so")
        _verlib(self, "libLTO.so.*")

    return install


@split("lld")
def _(self):
    self.subdesc = "linker"

    return lambda: _verbins(self, "lld", False)


@split("lld-default")
def _(self):
    self.subdesc = "linker default links"

    return lambda: _verbins(self, "lld", True)


@split("lld-devel-static")
def _(self):
    self.subdesc = "linker static libraries"
    self.depends = []
    self.install_if = []

    return lambda: _vergen(self, "lib/liblld*.a")


@split("lld-devel")
def _(self):
    self.subdesc = "linker development files"
    self.depends = [
        self.with_pkgver(f"llvm{_majver}-lld"),
        self.with_pkgver(f"llvm{_majver}-lld-devel-static"),
    ]

    def install():
        _vergen(self, "include/lld")
        _vergen(self, "lib/cmake/lld")

    return install


@split("devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return lambda: _vergen(self, "lib/*.a")


@split("devel")
def _(self):
    # unfortunately cmake files reference the static libs and force their
    # installation onto the target system, nothing much we can do about that
    self.depends = [
        self.parent,
        self.with_pkgver(f"llvm{_majver}-clang-tools-extra"),
        self.with_pkgver(f"llvm{_majver}-devel-static"),
        self.with_pkgver(f"llvm{_majver}-clang-cpp-libs"),
    ]
    # dumb llvmexports shit
    if _enable_mlir:
        self.depends.append(self.with_pkgver(f"llvm{_majver}-mlir"))
    if self.stage > 0:
        self.depends.append("zstd-devel")

    def install():
        _vergen(self, "include")
        _vergen(self, "lib/*.so")
        _vergen(self, "lib/libRemarks.so.*")
        _vergen(self, "lib/cmake")

    return install


@split("default")
def _(self):
    self.subdesc = "default links"

    # take all remaining unversioned links
    return lambda: _defbin(self, "*")
