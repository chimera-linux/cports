pkgname = "llvm"
pkgver = "18.1.8"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DENABLE_LINKER_BUILD_ID=YES",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=YES",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # avoid execinfo
    "-DCOMPILER_RT_BUILD_GWP_ASAN=NO",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=NO",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXX_HARDENING_MODE=fast",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=NO",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
    "-DLLVM_INSTALL_BINUTILS_SYMLINKS=YES",
    "-DLLVM_INSTALL_UTILS=YES",
    "-DLLVM_BUILD_LLVM_DYLIB=YES",
    "-DLLVM_LINK_LLVM_DYLIB=YES",
    "-DLLVM_ENABLE_RTTI=YES",
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=YES",
    "-DCLANG_DEFAULT_RTLIB=compiler-rt",
    "-DCLANG_DEFAULT_UNWINDLIB=libunwind",
    "-DCLANG_DEFAULT_CXX_STDLIB=libc++",
    "-DCLANG_CONFIG_FILE_SYSTEM_DIR=/etc/clang",
    "-DLLVM_ENABLE_LIBXML2=NO",
    "-DLLVM_ENABLE_LLD=YES",
    "-DLLVM_ENABLE_LIBCXX=YES",
    "-DLIBUNWIND_ENABLE_ASSERTIONS=OFF",
    "-DLIBUNWIND_USE_COMPILER_RT=YES",
    "-DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "python",
    "zlib-ng-compat-devel",
]
makedepends = ["zlib-ng-compat-devel", "libatomic-chimera-devel"]
depends = [
    f"llvm-libs={pkgver}-r{pkgrel}",
    f"llvm-binutils={pkgver}-r{pkgrel}",
    f"llvm-linker-tools={pkgver}-r{pkgrel}",
    f"llvm-runtime={pkgver}-r{pkgrel}",
]
pkgdesc = "Low Level Virtual Machine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "0b58557a6d32ceee97c8d533a59b9212d87e0fc4d2833924eb6c611247db2f2a"
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
    configure_args += ["-DLLVM_ENABLE_FFI=YES"]
    hostmakedepends += ["libffi-devel"]
    makedepends += [
        "python-devel",
        "libedit-devel",
        "libffi-devel",
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
        "-DLLVM_ENABLE_LIBEDIT=NO",
        "-DLLVM_ENABLE_LIBPFM=NO",
        "-DLLVM_ENABLE_TERMINFO=NO",
        # for stage 0 bootstrap, avoid all the optional runtime
        "-DCOMPILER_RT_BUILD_SANITIZERS=NO",
        "-DCOMPILER_RT_BUILD_XRAY=NO",
        "-DCOMPILER_RT_BUILD_LIBFUZZER=NO",
        "-DCOMPILER_RT_BUILD_PROFILE=NO",
        "-DCOMPILER_RT_BUILD_MEMPROF=NO",
    ]

_enable_flang = False
# from stage 2 only, pointless to build before
_enable_mlir = self.stage >= 2

match self.profile().arch:
    # consistently runs out of memory in flang ConvertExpr
    case "ppc64" | "riscv64":
        pass
    # unsupported on 32 bit cpus
    case "ppc" | "armhf" | "armv7":
        pass
    # elsewhere is okay
    case _:
        _enable_flang = _enable_mlir

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
        "-DCLANG_TABLEGEN=/usr/bin/clang-tblgen",
        "-DCLANG_PSEUDO_GEN=/usr/bin/clang-pseudo-gen",
        "-DCLANG_TIDY_CONFUSABLE_CHARS_GEN=/usr/bin/clang-tidy-confusable-chars-gen",
        "-DMLIR_TABLEGEN=/usr/bin/mlir-tblgen",
        "-DMLIR_PDLL_TABLEGEN=/usr/bin/mlir-pdll",
        "-DMLIR_LINALG_ODS_YAML_GEN=/usr/bin/mlir-linalg-ods-yaml-gen",
    ]


def do_configure(self):
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
        self.configure_args
        + [
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

    # we don't want debuginfod symlinks, these may be provided by actual
    # debuginfod from elfutils (and there is no need to alias them)
    self.uninstall("usr/bin/debuginfod")
    self.uninstall("usr/bin/debuginfod-find")

    # python bytecode cache
    if self.stage > 0:
        python.precompile(self, "usr/share/scan-view")

    # extra cross bins, not super useful outside of that but harmless
    self.install_bin("build/bin/clang-tidy-confusable-chars-gen")
    self.install_bin("build/bin/clang-pseudo-gen")


@subpackage("clang-tools-extra-static")
def _tools_extra_static(self):
    self.pkgdesc = f"{pkgdesc} (extra Clang tools static libraries)"
    self.depends = []
    self.install_if = []

    return [
        "usr/lib/libclangApplyReplacements*",
        "usr/lib/libclangQuery*",
        "usr/lib/libclangTidy*",
    ]


@subpackage("clang-tools-extra")
def _tools_extra(self):
    self.pkgdesc = f"{pkgdesc} (extra Clang tools)"
    self.depends = [
        f"clang={pkgver}-r{pkgrel}",
        f"clang-tools-extra-static={pkgver}-r{pkgrel}",
    ]

    return [
        "usr/include/clang-tidy",
        "usr/bin/clang-apply-replacements",
        "usr/bin/clang-query",
        "usr/bin/clang-pseudo-gen",
        "usr/bin/clang-rename",
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
def _binutils(self):
    self.pkgdesc = f"{pkgdesc} (binary manipulation tools)"
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
def _clang(self):
    self.pkgdesc = f"{pkgdesc} (C language family frontend)"
    self.depends = [
        f"libcxx-devel={pkgver}-r{pkgrel}",
        f"clang-rt-devel={pkgver}-r{pkgrel}",
        f"llvm-binutils={pkgver}-r{pkgrel}",
        "fortify-headers",
        "libatomic-chimera-devel",
        "musl-devel",
    ]

    return [
        "usr/bin/*clang*",
        "usr/bin/c-index-test",
        "usr/bin/cc",
        "usr/bin/c89",
        "usr/bin/c99",
        "usr/bin/c++",
        "usr/lib/cmake/clang",
        "usr/share/clang",
    ]


@subpackage("clang-rt-devel")
def _clang_rt_devel(self):
    self.pkgdesc = f"{pkgdesc} (Clang runtime development files)"
    self.options = ["ltostrip", "!splitstatic"]  # these are explicitly -fno-lto

    return ["usr/lib/clang"]


@subpackage("clang-devel-static")
def _clang_static(self):
    self.pkgdesc = f"{pkgdesc} (Clang static libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/libclang*.a"]


@subpackage("clang-devel")
def _clang_devel(self):
    self.pkgdesc = f"{pkgdesc} (Clang development files)"
    # unfortunately cmake files reference the static libs and force their
    # installation onto the target system, nothing much we can do about that
    self.depends = [
        f"clang-rt-devel={pkgver}-r{pkgrel}",
        f"clang-devel-static={pkgver}-r{pkgrel}",
        f"clang-libs={pkgver}-r{pkgrel}",
        f"clang-cpp-libs={pkgver}-r{pkgrel}",
        f"libcxx-devel={pkgver}-r{pkgrel}",
    ]

    return [
        "usr/include/clang",
        "usr/include/clang-c",
        "usr/lib/libclang*.so",
    ]


@subpackage("clang-analyzer")
def _clang_analyzer(self):
    self.pkgdesc = f"{pkgdesc} (source code analysis)"
    self.depends = [f"clang={pkgver}-r{pkgrel}"]
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
def _libclang(self):
    self.pkgdesc = f"{pkgdesc} (C frontend runtime library)"
    self.provides = [f"libclang={pkgver}-r{pkgrel}"]

    return ["usr/lib/libclang.so.*"]


@subpackage("clang-cpp-libs")
def _libclang_cpp(self):
    self.pkgdesc = f"{pkgdesc} (C frontend runtime library)"
    self.provides = [f"libclang-cpp={pkgver}-r{pkgrel}"]

    return ["usr/lib/libclang-cpp.so.*"]


@subpackage("flang", _enable_flang)
def _flang(self):
    self.pkgdesc = f"{pkgdesc} (Fortran frontend)"
    self.depends = [
        f"clang={pkgver}-r{pkgrel}",
        f"flang-devel={pkgver}-r{pkgrel}",
    ]

    return [
        "usr/bin/bbc",
        "usr/bin/f18*",
        "usr/bin/fir*",
        "usr/bin/flang*",
        "usr/bin/tco",
    ]


@subpackage("flang-devel-static", _enable_flang)
def _flang_devel_static(self):
    self.pkgdesc = f"{pkgdesc} (Flang static libraries)"
    self.depends = []
    self.install_if = []

    return [
        "usr/lib/libFIR*.a",
        "usr/lib/libflang*.a",
        "usr/lib/libFortran*.a",
        "usr/lib/libHLFIR*.a",
    ]


@subpackage("flang-devel", _enable_flang)
def _flang_devel(self):
    self.pkgdesc = f"{pkgdesc} (Flang development files)"
    self.depends = [f"flang-devel-static={pkgver}-r{pkgrel}"]

    return [
        "usr/include/flang",
        "usr/lib/cmake/flang",
    ]


@subpackage("mlir", _enable_mlir)
def _mlir(self):
    self.pkgdesc = f"{pkgdesc} (MLIR)"

    return ["usr/bin/mlir*"]


@subpackage("mlir-devel-static", _enable_mlir)
def _mlir_static(self):
    self.pkgdesc = f"{pkgdesc} (MLIR static libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/libMLIR*.a"]


@subpackage("mlir-devel", _enable_mlir)
def _mlir_devel(self):
    self.pkgdesc = f"{pkgdesc} (MLIR development files)"
    self.depends = [f"mlir-devel-static={pkgver}-r{pkgrel}"]

    return [
        "usr/include/mlir*",
        "usr/lib/libMLIR.so",
        "usr/lib/libmlir*.so",
        "usr/lib/cmake/mlir",
    ]


@subpackage("mlir-libs", _enable_mlir)
def _libmlir(self):
    self.pkgdesc = f"{pkgdesc} (MLIR runtime libraries)"
    self.provides = [f"libmlir={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/libMLIR.so.*",
        "usr/lib/libmlir*.so.*",
    ]


@subpackage("libunwind")
def _libunwind(self):
    self.pkgdesc = f"{pkgdesc} (libunwind)"

    return ["usr/lib/libunwind.so.*"]


@subpackage("libunwind-devel-static")
def _libunwind_static(self):
    self.pkgdesc = f"{pkgdesc} (libunwind) (static library)"
    self.options = ["ltostrip"]

    return ["usr/lib/libunwind.a"]


@subpackage("libunwind-devel")
def _libunwind_devel(self):
    self.pkgdesc = f"{pkgdesc} (libunwind) (development files)"

    return [
        "usr/lib/libunwind.so",
        "usr/include/*unwind*",
        "usr/include/mach-o",
    ]


@subpackage("libcxx")
def _libcxx(self):
    self.pkgdesc = f"{pkgdesc} (C++ standard library)"

    return ["usr/lib/libc++.so.*"]


@subpackage("libcxx-devel-static")
def _libcxx_static(self):
    self.pkgdesc = f"{pkgdesc} (C++ standard library) (static library)"
    self.depends += [f"libcxxabi-devel-static={pkgver}-r{pkgrel}"]
    self.options = ["ltostrip"]

    return ["usr/lib/libc++.a"]


@subpackage("libcxxabi-devel")
def _libcxxabi_devel(self):
    self.pkgdesc = f"{pkgdesc} (low level C++ runtime) (development files)"
    self.depends = [f"libunwind-devel={pkgver}-r{pkgrel}"]

    return [
        "usr/include/c++/v1/cxxabi.h",
        "usr/include/c++/v1/__cxxabi_config.h",
        "usr/lib/libc++abi.so",
    ]


@subpackage("libcxx-devel")
def _libcxx_devel(self):
    self.pkgdesc = f"{pkgdesc} (C++ standard library) (development files)"
    self.depends = [f"libcxxabi-devel={pkgver}-r{pkgrel}"]
    self.options = ["ltostrip", "!splitstatic"]

    return [
        "usr/lib/libc++.so",
        "usr/lib/libc++experimental.a",
        "usr/include/c++",
    ]


@subpackage("libcxxabi")
def _libcxxabi(self):
    self.pkgdesc = f"{pkgdesc} (low level C++ runtime)"
    self.depends = [f"libunwind={pkgver}-r{pkgrel}"]

    return ["usr/lib/libc++abi.so.*"]


@subpackage("libcxxabi-devel-static")
def _libcxxabi_static(self):
    self.pkgdesc = f"{pkgdesc} (low level C++ runtime) (static library)"
    self.depends += [f"libunwind-devel-static={pkgver}-r{pkgrel}"]
    self.options = ["ltostrip"]

    return ["usr/lib/libc++abi.a"]


@subpackage("llvm-libs")
def _libllvm(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"
    self.provides = [f"libllvm={pkgver}-r{pkgrel}"]

    return ["usr/lib/libLLVM.so.*", f"usr/lib/libLLVM-{_llvmgen}*.so"]


@subpackage("lld")
def _lld(self):
    self.pkgdesc = f"{pkgdesc} (linker)"
    self.install_if = [f"clang={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/ld",
        "usr/bin/lld*",
        "usr/bin/wasm-ld",
        "usr/bin/ld.lld*",
        "usr/bin/ld64.lld*",
    ]


@subpackage("lld-devel-static")
def _lld_devel_static(self):
    self.pkgdesc = f"{pkgdesc} (linker) (static libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/liblld*.a"]


@subpackage("lld-devel")
def _lld_devel(self):
    self.pkgdesc = f"{pkgdesc} (linker) (development files)"
    self.depends = [
        f"lld={pkgver}-r{pkgrel}",
        f"lld-devel-static={pkgver}-r{pkgrel}",
    ]

    return [
        "usr/include/lld",
        "usr/lib/cmake/lld",
    ]


@subpackage("llvm-linker-tools")
def _llvm_linker_tools(self):
    self.pkgdesc = f"{pkgdesc} (linker plugins)"

    return ["usr/lib/libLTO.so.*"]


@subpackage("llvm-devel-static")
def _llvm_static(self):
    self.pkgdesc = "Low Level Virtual Machine (static libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("llvm-devel")
def _llvm_devel(self):
    # unfortunately cmake files reference the static libs and force their
    # installation onto the target system, nothing much we can do about that
    self.depends = [
        f"llvm={pkgver}-r{pkgrel}",
        f"llvm-tools={pkgver}-r{pkgrel}",
        f"llvm-devel-static={pkgver}-r{pkgrel}",
        f"clang-cpp-libs={pkgver}-r{pkgrel}",
    ]
    # dumb llvmexports shit
    if _enable_mlir:
        self.depends.append(f"mlir={pkgver}-r{pkgrel}")
    if self.stage > 0:
        self.depends.append("zstd-devel")

    return [
        "usr/include",
        "usr/lib/*.so",
        "usr/lib/libRemarks.so.*",
        "usr/lib/cmake",
    ]


@subpackage("llvm-tools")
def _llvm_tools(self):
    self.pkgdesc = f"{pkgdesc} (testing tools)"

    return [
        "usr/bin/FileCheck",
        "usr/bin/count",
        "usr/bin/not",
        "usr/bin/split-file",
        "usr/bin/yaml-bench",
        "usr/share/opt-viewer",
    ]


@subpackage("llvm-runtime")
def _llvm_runtime(self):
    self.pkgdesc = f"{pkgdesc} (runtime)"

    return [
        "usr/bin/lli*",
    ]
