pkgname = "llvm"
pkgver = "20.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
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
    "-DLLVM_ENABLE_LLD=ON",
    "-DLLVM_ENABLE_LIBCXX=ON",
    "-DLIBUNWIND_ENABLE_ASSERTIONS=OFF",
    "-DLIBUNWIND_USE_COMPILER_RT=ON",
    "-DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF",
]
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
    self.with_pkgver("llvm-libs"),
    self.with_pkgver("llvm-binutils"),
    self.with_pkgver("llvm-linker-tools"),
    self.with_pkgver("llvm-runtime"),
]
pkgdesc = "Low Level Virtual Machine"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "6898f963c8e938981e6c4a302e83ec5beb4630147c7311183cf61069af16333d"
# reduce size of debug symbols
debug_level = 1
# lto does not kick in until stage 2
# tests are not enabled
# runtimes build may invoke built clang during install, which has
# rpath and fakeroot effectively overrides rpath, so disable that
options = ["bootstrap", "!check", "!installroot"]

# disable ubsan integer checks, it breaks aarch64/riscv64/ppc64 targets
# when lto-linking lld with ubsan'd clang/lld, it causes
# that to crash in 'AArch64 Instruction Selection'
# (on ppc64le, 'PowerPC Instruction Selection' e.g.
# when building graphviz)
# while on riscv it prevents rust from building
hardening = ["!int"]

_llvmgen = pkgver[0 : pkgver.find(".")]

cmake_dir = "llvm"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
    "LDFLAGS": [],
}

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
    if self.stage >= 2:
        # also use llvm-bootstrap
        if not self.profile().cross:
            hostmakedepends += ["llvm-bootstrap"]
            # set all the stuff that matters
            configure_args += [
                "-DCMAKE_AR=/usr/lib/llvm-bootstrap/bin/llvm-ar",
                "-DCMAKE_NM=/usr/lib/llvm-bootstrap/bin/llvm-nm",
                "-DCMAKE_RANLIB=/usr/lib/llvm-bootstrap/bin/llvm-ranlib",
            ]
            tool_flags["LDFLAGS"] += [
                "-fuse-ld=/usr/lib/llvm-bootstrap/bin/ld.lld"
            ]
        else:
            hostmakedepends += ["llvm", "clang-tools-extra", "mlir"]
else:
    configure_args += [
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
_enable_mlir = self.stage >= 2
_enable_flang = _enable_mlir and self.profile().wordsize == 64

if _enable_mlir:
    _enabled_projects += ["mlir"]

if _enable_flang:
    _enabled_projects += ["flang"]

match self.profile().arch:
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
        broken = f"Unknown CPU architecture: {self.profile().arch}"

configure_args += [f"-DLLVM_ENABLE_PROJECTS={';'.join(_enabled_projects)}"]
configure_args += [f"-DLLVM_ENABLE_RUNTIMES={';'.join(_enabled_runtimes)}"]


def init_configure(self):
    if self.has_lto():
        self.configure_args += ["-DLLVM_ENABLE_LTO=Thin"]

    if not self.profile().cross:
        if self.stage >= 2:
            self.configure_args += [
                f"-DCMAKE_C_COMPILER={self.chroot_cwd / 'boot-clang'}",
                f"-DCMAKE_CXX_COMPILER={self.chroot_cwd / 'boot-clang++'}",
            ]
        return

    # grab these from the host
    self.configure_args += [
        "-DLLVM_NATIVE_TOOL_DIR=/usr/bin",
        "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
        "-DLLVM_TABLEGEN=/usr/bin/llvm-tblgen",
        "-DLLVM_HEADERS_TABLEGEN=/usr/bin/llvm-tblgen",
        "-DCLANG_TABLEGEN=/usr/bin/clang-tblgen",
        "-DCLANG_TIDY_CONFUSABLE_CHARS_GEN=/usr/bin/clang-tidy-confusable-chars-gen",
        "-DMLIR_TABLEGEN=/usr/bin/mlir-tblgen",
        "-DMLIR_PDLL_TABLEGEN=/usr/bin/mlir-pdll",
        "-DMLIR_MLIR_SRC_SHARDER_TABLEGEN=/usr/bin/mlir-src-sharder",
        "-DMLIR_LINALG_ODS_YAML_GEN=/usr/bin/mlir-linalg-ods-yaml-gen",
    ]


def configure(self):
    from cbuild.util import cmake

    # when bootstrapping, this will check the actual profile
    with self.profile(self.profile().arch) as pf:
        trip = pf.triplet

    for f in ["clang", "clang++"]:
        outp = self.cwd / f"boot-{f}"
        if not self.use_ccache:
            outp.symlink_to(f"/usr/lib/llvm-bootstrap/bin/{f}")
            continue
        with open(outp, "w") as outf:
            outf.write(
                f"""#!/bin/sh
exec /usr/bin/ccache /usr/lib/llvm-bootstrap/bin/{f} "$@"
"""
            )
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

    # it's our default toolchain
    self.install_link("usr/bin/cc", "clang")
    self.install_link("usr/bin/c++", "clang++")
    if not (self.destdir / "usr/bin/ld").is_symlink():
        self.install_link("usr/bin/ld", "ld.lld")
    # posix mandates this
    self.install_bin(self.files_path / "c99")
    # widely provided though not required anymore
    self.install_bin(self.files_path / "c89")

    # make stage0 bootstrap profile happy
    with self.profile(self.profile().arch) as pf:
        trip = pf.triplet

    # arch-prefixed symlinks for cross consistency (no config file)
    self.install_link(f"usr/bin/{trip}-clang", "clang")
    self.install_link(f"usr/bin/{trip}-clang++", "clang++")
    self.install_link(f"usr/bin/{trip}-clang-cpp", "clang-cpp")
    self.install_link(f"usr/bin/{trip}-cc", "cc")
    self.install_link(f"usr/bin/{trip}-c++", "c++")
    self.install_link(f"usr/bin/{trip}-ld", "ld")
    self.install_link(f"usr/bin/{trip}-ld.lld", "ld.lld")

    self.install_license("LICENSE.TXT")

    # we don't want debuginfod symlinks, these may be provided by actual
    # debuginfod from elfutils (and there is no need to alias them)
    self.uninstall("usr/bin/debuginfod")
    self.uninstall("usr/bin/debuginfod-find")

    # python bytecode cache
    if self.stage > 0:
        python.precompile(self, "usr/share/scan-view")

    # extra cross bins, not super useful outside of that but harmless
    self.install_bin("build/bin/clang-tidy-confusable-chars-gen")
    # FIXME: make it build for cross so we get consistent packages
    if _enable_mlir and not self.profile().cross:
        self.install_bin("build/bin/mlir-src-sharder")


@subpackage("clang-tools-extra-static")
def _(self):
    self.subdesc = "extra Clang tools static libraries"
    self.depends = []
    self.install_if = []

    return [
        "usr/lib/libclangApplyReplacements*",
        "usr/lib/libclangQuery*",
        "usr/lib/libclangTidy*",
    ]


@subpackage("clang-tools-extra")
def _(self):
    self.subdesc = "extra Clang tools"
    self.depends = [
        self.with_pkgver("clang"),
        self.with_pkgver("clang-tools-extra-static"),
    ]

    return [
        "usr/include/clang-tidy",
        "usr/bin/clang-apply-replacements",
        "usr/bin/clang-query",
        "usr/bin/clang-tidy",
        "usr/bin/clang-tidy-confusable-chars-gen",
        "usr/bin/diagtool",
        "usr/bin/find-all-symbols",
        "usr/bin/hmaptool",
        "usr/bin/modularize",
        "usr/bin/pp-trace",
        "usr/bin/run-clang-tidy",
        "usr/bin/sancov",
        "usr/share/clang/*tidy*",
    ]


@subpackage("llvm-binutils")
def _(self):
    self.subdesc = "binary manipulation tools"
    # prevent file conflict errors, we're dropping this
    self.replaces = ["elftoolchain<0.7.1_svn20230501"]

    return [
        "usr/bin/addr2line",
        "usr/bin/ar",
        "usr/bin/c++filt",
        "usr/bin/dlltool",
        "usr/bin/dwp",
        "usr/bin/llvm-addr2line",
        "usr/bin/llvm-ar",
        "usr/bin/llvm-bitcode-strip",
        "usr/bin/llvm-cxxfilt",
        "usr/bin/llvm-dlltool",
        "usr/bin/llvm-dwp",
        "usr/bin/llvm-install-name-tool",
        "usr/bin/llvm-lib",
        "usr/bin/llvm-nm",
        "usr/bin/llvm-objcopy",
        "usr/bin/llvm-objdump",
        "usr/bin/llvm-ranlib",
        "usr/bin/llvm-rc",
        "usr/bin/llvm-readelf",
        "usr/bin/llvm-readobj",
        "usr/bin/llvm-size",
        "usr/bin/llvm-strings",
        "usr/bin/llvm-strip",
        "usr/bin/llvm-symbolizer",
        "usr/bin/nm",
        "usr/bin/objcopy",
        "usr/bin/objdump",
        "usr/bin/ranlib",
        "usr/bin/readelf",
        "usr/bin/size",
        "usr/bin/strings",
        "usr/bin/strip",
        "usr/bin/windres",
    ]


@subpackage("clang")
def _(self):
    self.subdesc = "C language family frontend"
    self.depends = [
        self.with_pkgver("libcxx-devel"),
        self.with_pkgver("clang-rt-devel"),
        self.with_pkgver("llvm-binutils"),
        "fortify-headers",
        "libatomic-chimera-devel",
        "musl-devel",
    ]

    return [
        "usr/bin/*clang*",
        "usr/bin/*-cc",
        "usr/bin/*-c++",
        "usr/bin/c-index-test",
        "usr/bin/cc",
        "usr/bin/c89",
        "usr/bin/c99",
        "usr/bin/c++",
        "usr/lib/cmake/clang",
        "usr/share/clang",
        "usr/share/clang-doc",
    ]


@subpackage("clang-rt-devel")
def _(self):
    self.subdesc = "Clang runtime development files"
    self.options = ["ltostrip", "!splitstatic"]  # these are explicitly -fno-lto

    return ["usr/lib/clang"]


@subpackage("clang-devel-static")
def _(self):
    self.subdesc = "Clang static libraries"
    self.depends = []
    self.install_if = []

    return ["usr/lib/libclang*.a"]


@subpackage("clang-devel")
def _(self):
    self.subdesc = "Clang development files"
    # unfortunately cmake files reference the static libs and force their
    # installation onto the target system, nothing much we can do about that
    self.depends = [
        self.with_pkgver("clang-rt-devel"),
        self.with_pkgver("clang-devel-static"),
        self.with_pkgver("clang-libs"),
        self.with_pkgver("clang-cpp-libs"),
        self.with_pkgver("libcxx-devel"),
    ]

    return [
        "usr/include/clang",
        "usr/include/clang-c",
        "usr/lib/libclang*.so",
    ]


@subpackage("clang-analyzer")
def _(self):
    self.subdesc = "source code analysis"
    self.depends = [self.with_pkgver("clang")]
    if self.stage > 0:
        self.depends += ["perl", "python"]

    return [
        "usr/bin/analyze-build",
        "usr/bin/intercept-build",
        "usr/bin/scan-*",
        "usr/lib/libear",
        "usr/lib/libscanbuild",
        "usr/libexec/analyze-*",
        "usr/libexec/*analyzer",
        "usr/libexec/intercept-*",
        "usr/share/scan-*",
        "usr/share/man/man1/scan-build.1",
    ]


@subpackage("clang-libs")
def _(self):
    self.subdesc = "Clang runtime library"
    self.provides = [self.with_pkgver("libclang")]

    return ["usr/lib/libclang.so.*"]


@subpackage("clang-cpp-libs")
def _(self):
    self.subdesc = "Clang C++ runtime library"
    self.provides = [self.with_pkgver("libclang-cpp")]

    return ["usr/lib/libclang-cpp.so.*"]


@subpackage("flang", _enable_flang)
def _(self):
    self.subdesc = "Fortran frontend"
    self.depends = [
        self.with_pkgver("clang"),
        self.with_pkgver("flang-devel"),
    ]

    return [
        "usr/bin/bbc",
        "usr/bin/f18*",
        "usr/bin/fir*",
        "usr/bin/flang*",
        "usr/bin/tco",
    ]


@subpackage("flang-devel-static", _enable_flang)
def _(self):
    self.subdesc = "Flang static libraries"
    self.depends = []
    self.install_if = []

    return [
        "usr/lib/libFIR*.a",
        "usr/lib/libflang*.a",
        "usr/lib/libFortran*.a",
        "usr/lib/libHLFIR*.a",
    ]


@subpackage("flang-devel", _enable_flang)
def _(self):
    self.subdesc = "Flang development files"
    self.depends = [self.with_pkgver("flang-devel-static")]

    return [
        "usr/include/flang",
        "usr/lib/cmake/flang",
    ]


@subpackage("mlir", _enable_mlir)
def _(self):
    self.subdesc = "MLIR"

    return ["usr/bin/mlir*"]


@subpackage("mlir-devel-static", _enable_mlir)
def _(self):
    self.subdesc = "MLIR static libraries"
    self.depends = []
    self.install_if = []

    return ["usr/lib/libMLIR*.a"]


@subpackage("mlir-devel", _enable_mlir)
def _(self):
    self.subdesc = "MLIR development files"
    self.depends = [self.with_pkgver("mlir-devel-static")]

    return [
        "usr/include/mlir*",
        "usr/lib/libMLIR*.so",
        "usr/lib/libmlir*.so",
        "usr/lib/cmake/mlir",
    ]


@subpackage("mlir-libs", _enable_mlir)
def _(self):
    self.subdesc = "MLIR runtime libraries"
    self.provides = [self.with_pkgver("libmlir")]

    return [
        "usr/lib/libMLIR*.so.*",
        "usr/lib/libmlir*.so.*",
    ]


@subpackage("libunwind")
def _(self):
    self.subdesc = "libunwind"
    self.compression = "deflate"

    return ["usr/lib/libunwind.so.*"]


@subpackage("libunwind-devel-static")
def _(self):
    self.subdesc = "libunwind static library"
    self.options = ["ltostrip"]

    return ["usr/lib/libunwind.a"]


@subpackage("libunwind-devel")
def _(self):
    self.subdesc = "libunwind development files"

    return [
        "usr/lib/libunwind.so",
        "usr/include/*unwind*",
        "usr/include/mach-o",
    ]


@subpackage("libcxx")
def _(self):
    self.subdesc = "C++ standard library"
    self.compression = "deflate"

    return ["usr/lib/libc++.so.*"]


@subpackage("libcxx-devel-static")
def _(self):
    self.subdesc = "C++ standard library static library"
    self.depends += [self.with_pkgver("libcxxabi-devel-static")]
    self.options = ["ltostrip"]

    return ["usr/lib/libc++.a"]


@subpackage("libcxxabi-devel")
def _(self):
    self.subdesc = "low level C++ runtime development files"
    self.depends = [self.with_pkgver("libunwind-devel")]

    return [
        "usr/include/c++/v1/cxxabi.h",
        "usr/include/c++/v1/__cxxabi_config.h",
        "usr/lib/libc++abi.so",
    ]


@subpackage("libcxx-devel")
def _(self):
    self.subdesc = "C++ standard library development files"
    self.depends = [self.with_pkgver("libcxxabi-devel")]
    self.options = ["ltostrip", "!splitstatic"]

    return [
        "usr/lib/libc++.modules.json",
        "usr/lib/libc++.so",
        "usr/lib/libc++experimental.a",
        "usr/include/c++",
        "usr/share/libc++",
    ]


@subpackage("libcxxabi")
def _(self):
    self.subdesc = "low level C++ runtime"
    self.depends = [self.with_pkgver("libunwind")]
    self.compression = "deflate"

    return ["usr/lib/libc++abi.so.*"]


@subpackage("libcxxabi-devel-static")
def _(self):
    self.subdesc = "low level C++ runtime static library"
    self.depends += [self.with_pkgver("libunwind-devel-static")]
    self.options = ["ltostrip"]

    return ["usr/lib/libc++abi.a"]


@subpackage("llvm-libs")
def _(self):
    self.provides = [self.with_pkgver("libllvm")]

    return ["usr/lib/libLLVM.so.*", f"usr/lib/libLLVM-{_llvmgen}*.so"]


@subpackage("lld")
def _(self):
    self.subdesc = "linker"
    self.install_if = [self.with_pkgver("clang")]

    return [
        "usr/bin/*-ld*",
        "usr/bin/ld",
        "usr/bin/lld*",
        "usr/bin/ld.lld*",
        "usr/bin/ld64.lld*",
    ]


@subpackage("lld-devel-static")
def _(self):
    self.subdesc = "linker static libraries"
    self.depends = []
    self.install_if = []

    return ["usr/lib/liblld*.a"]


@subpackage("lld-devel")
def _(self):
    self.subdesc = "linker development files"
    self.depends = [
        self.with_pkgver("lld"),
        self.with_pkgver("lld-devel-static"),
    ]

    return [
        "usr/include/lld",
        "usr/lib/cmake/lld",
    ]


@subpackage("llvm-linker-tools")
def _(self):
    self.subdesc = "linker plugins"

    return ["usr/lib/libLTO.so.*"]


@subpackage("llvm-devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("llvm-devel")
def _(self):
    # unfortunately cmake files reference the static libs and force their
    # installation onto the target system, nothing much we can do about that
    self.depends = [
        self.parent,
        self.with_pkgver("llvm-tools"),
        self.with_pkgver("llvm-devel-static"),
        self.with_pkgver("clang-cpp-libs"),
    ]
    # dumb llvmexports shit
    if _enable_mlir:
        self.depends.append(self.with_pkgver("mlir"))
    if self.stage > 0:
        self.depends.append("zstd-devel")

    return [
        "usr/include",
        "usr/lib/*.so",
        "usr/lib/libRemarks.so.*",
        "usr/lib/cmake",
    ]


@subpackage("llvm-tools")
def _(self):
    self.subdesc = "testing tools"

    return [
        "usr/bin/FileCheck",
        "usr/bin/count",
        "usr/bin/not",
        "usr/bin/split-file",
        "usr/bin/yaml-bench",
        "usr/share/opt-viewer",
    ]


@subpackage("llvm-runtime")
def _(self):
    self.subdesc = "runtime"

    return [
        "usr/bin/lli*",
    ]
