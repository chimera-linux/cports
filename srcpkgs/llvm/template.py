pkgname = "llvm"
_mver = "12"
version = f"{_mver}.0.0"
revision = 0
wrksrc = f"llvm-project-{version}.src"
build_style = "cmake"
configure_args = [
    # don't enable lldb for now, we don't package enough for it
    "-DLLVM_ENABLE_PROJECTS=clang;clang-tools-extra;compiler-rt;libcxx;libcxxabi;libunwind;lld;openmp",
    # other stuff
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=YES",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=YES",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
    "-DLIBOMP_ENABLE_SHARED=YES",
    "-DLIBOMP_INSTALL_ALIASES=NO",
    "-DLLVM_INSTALL_UTILS=YES",
    "-DLLVM_BUILD_LLVM_DYLIB=YES",
    "-DLLVM_LINK_LLVM_DYLIB=YES",
    "-DLLVM_ENABLE_RTTI=YES",
    "-DLLVM_ENABLE_FFI=YES",
    "-DCLANG_DEFAULT_RTLIB=compiler-rt",
    "-DCLANG_DEFAULT_UNWINDLIB=libunwind",
    "-DCLANG_DEFAULT_CXX_STDLIB=libc++",
    "-DLLVM_ENABLE_LIBXML2=NO",
    "-DLLVM_ENABLE_LLD=YES",
    "-DLLVM_ENABLE_LIBCXX=YES",
]
makedepends = ["zlib-devel", "libffi-devel"]
depends = [
    f"libllvm={version}-r{revision}",
    f"libomp={version}-r{revision}",
    f"llvm-linker-tools={version}-r{revision}",
    f"llvm-runtime={version}-r{revision}"
]
make_cmd = "make"
short_desc = "Low Level Virtual Machine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://llvm.org"
distfiles = [f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz"]
checksum = ["9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628"]

options = ["bootstrap"]

cmake_dir = "llvm"

CFLAGS = ["-fPIC"]
CXXFLAGS = ["-fPIC"]

if not current.bootstrapping:
    hostmakedepends = [
        "cmake", "pkgconf", "perl", "python", "zlib-devel", "libffi-devel"
    ]
    makedepends += [
        "python-devel", "libedit-devel", "elftoolchain-devel",
        "libexecinfo-devel"
    ]
    depends += ["libexecinfo-devel"]
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

from cbuild import cpu

_triplet, _arch = cpu.match_target(
    "x86_64*", ("x86_64-linux-musl", "X86"),
    "aarch64*", ("aarch64-linux-musl", "AArch64"),
    "ppc64le*", ("powerpc64le-linux-musl", "PowerPC"),
    "ppc64*", ("powerpc64-linux-musl", "PowerPC"),
    "riscv64*", ("riscv64-linux-musl", "RISCV64"),
)

def init_configure(self):
    if not self.cross_build:
        return

    self.configure_args.append("-DLLVM_TABLEGEN=" + str(self.chroot_wrksrc / "build_host/bin/llvm-tblgen"))
    self.configure_args.append("-DCLANG_TABLEGEN=" + str(self.chroot_wrksrc / "build_host/bin/clang-tblgen"))

def pre_configure(self):
    if not self.cross_build:
        return

    from cbuild.util import make, cmake

    self.log("building host tblgen...")

    with self.profile(cpu.host()):
        with self.stamp("host_llvm_configure"):
            cmake.configure(self, self.cmake_dir, "build_host")

        with self.stamp("host_llvm_tblgen") as s:
            s.check()
            make.Make(self, wrksrc = "build_host").build([
                "-C", "utils/TableGen"
            ])

        with self.stamp("host_clang_tblgen") as s:
            s.check()
            make.Make(self, wrksrc = "build_host").build([
                "-C", "tools/clang/utils/TableGen"
            ])

def do_configure(self):
    from cbuild.util import cmake

    cmake.configure(self, self.cmake_dir, "build", [
        "-DLLVM_TARGET_ARCH=" + _arch,
        "-DLLVM_HOST_TRIPLE=" + _triplet,
        "-DLLVM_DEFAULT_TARGET_TRIPLE=" + _triplet,
    ])

def post_install(self):
    self.install_file(
        self.abs_wrksrc / "libcxxabi/include/__cxxabi_config.h", "usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libcxxabi/include/cxxabi.h", "usr/include"
    )

    self.install_dir("usr/include/mach-o")
    self.install_file(
        self.abs_wrksrc / "libunwind/include/__libunwind_config.h", "usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libunwind/include/libunwind.h", "usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libunwind/include/unwind.h", "usr/include"
    )
    self.install_file(
        self.abs_wrksrc / "libunwind/include/mach-o/compact_unwind_encoding.h",
        "usr/include/mach-o"
    )
    # it's our default toolchain
    self.install_link("clang", "usr/bin/cc")
    self.install_link("clang++", "usr/bin/c++")
    if not (self.destdir / "usr/bin/ld").is_symlink():
        self.install_link("ld.lld", "usr/bin/ld")

@subpackage("clang-tools-extra")
def _tools_extra(self):
    self.short_desc = short_desc + " - extra Clang tools"
    self.depends = [f"clang={version}-r{revision}"]

    return [
        "usr/include/clang-tidy",
        "usr/bin/clang-apply-replacements",
        "usr/bin/clang-query",
        "usr/bin/clang-rename",
        "usr/bin/clang-tidy",
        "usr/bin/diagtool",
        "usr/bin/find-all-symbols",
        "usr/bin/hmaptool",
        "usr/bin/modularize",
        "usr/bin/pp-trace",
        "usr/bin/sancov",
        "usr/lib/libclangApplyReplacements*",
        "usr/lib/libclangQuery*",
        "usr/lib/libclangTidy*",
        "usr/share/clang/*tidy*"
    ]

@subpackage("libomp")
def _libomp(self):
    self.short_desc = short_desc + " - Clang OpenMP support library"

    if not self.bootstrapping and _arch != "RISCV64":
        extra = ["usr/lib/libomptarget.rtl.*.so"]
    else:
        extra = []

    return [
        "usr/lib/libomp.so",
        "usr/lib/libarcher.so",
        "usr/lib/libomp*.so.*"
    ] + extra

@subpackage("libomp-devel")
def _libomp_devel(self):
    self.short_desc = short_desc + " - Clang OpenMP support library - development files"
    self.depends = [f"libomp={version}-r{revision}"]

    return [
        "usr/lib/libomp*.so",
        "usr/lib/libarcher*",
        "usr/include/omp*.h",
        f"usr/lib/clang/{version}/include/omp*.h"
    ]

@subpackage("clang")
def _clang(self):
    self.short_desc = short_desc + " - C language family frontend"
    self.depends = [
        f"libcxx-devel={version}-r{revision}",
        f"libcxxabi-devel={version}-r{revision}",
        f"clang-rt-devel={version}-r{revision}",
        "elftoolchain",
        "musl-devel",
    ]

    return [
        "usr/bin/*clang*",
        "usr/bin/c-index-test",
        "usr/bin/cc",
        "usr/bin/c++",
        "usr/lib/cmake/clang",
        "usr/share/clang"
    ]

@subpackage("clang-rt-devel")
def _clang_rt_devel(self):
    self.short_desc = short_desc + " - clang runtime development files"

    return [
        "usr/lib/clang"
    ]

@subpackage("clang-devel")
def _clang_devel(self):
    self.short_desc = short_desc + " - clang development files"
    self.depends = [
        f"clang-rt-devel={version}-r{revision}",
        f"libclang={version}-r{revision}",
        f"libclang-cpp={version}-r{revision}",
        f"libcxx-devel={version}-r{revision}"
    ]

    return [
        "usr/include/clang",
        "usr/include/clang-c",
        "usr/lib/libclang*.a",
        "usr/lib/libclang*.so",
    ]

@subpackage("clang-analyzer")
def _clang_analyzer(self):
    self.short_desc = short_desc + " - Source code analysis"
    self.depends = [f"clang={version}-r{revision}"]
    if not self.bootstrapping:
        self.depends.append("python")

    return [
        "usr/bin/scan-*",
        "usr/share/scan-*",
        "usr/libexec/*analyzer",
    ]

@subpackage("libclang")
def _libclang(self):
    self.short_desc = short_desc + " - C frontend runtime library"

    return ["usr/lib/libclang.so.*"]

@subpackage("libclang-cpp")
def _libclang_cpp(self):
    self.short_desc = short_desc + " - C frontend runtime library"

    return ["usr/lib/libclang-cpp.so.*"]

@subpackage("libunwind")
def _libunwind(self):
    self.short_desc = short_desc + " - libunwind"

    return ["usr/lib/libunwind.so.*"]

@subpackage("libunwind-devel")
def _libunwind_devel(self):
    self.short_desc = short_desc + " - libunwind - development files"
    self.depends = [f"libunwind={version}-r{revision}"]

    return [
        "usr/lib/libunwind.so",
        "usr/lib/libunwind.a",
        "usr/include/*unwind*",
        "usr/include/mach-o"
    ]

@subpackage("libcxx")
def _libcxx(self):
    self.short_desc = short_desc + " - C++ standard library"

    return ["usr/lib/libc++.so.*"]

@subpackage("libcxx-devel")
def _libcxx_devel(self):
    self.short_desc = short_desc + " - C++ standard library - development files"
    self.depends = [f"libcxx={version}-r{revision}"]

    return [
        "usr/lib/libc++.so",
        "usr/lib/libc++.a",
        "usr/lib/libc++experimental.a",
        "usr/include/c++",
    ]

@subpackage("libcxxabi")
def _libcxxabi(self):
    self.short_desc = short_desc + " - low level libc++ runtime"
    self.depends = [f"libunwind={version}-r{revision}"]

    return ["usr/lib/libc++abi.so.*"]

@subpackage("libcxxabi-devel")
def _libcxxabi_devel(self):
    self.short_desc = short_desc + " - low level libc++ runtime - development files"
    self.depends = [
        f"libcxxabi={version}-r{revision}",
        f"libunwind-devel={version}-r{revision}"
    ]

    return [
        "usr/lib/libc++abi.so",
        "usr/lib/libc++abi.a",
        "usr/include/*cxxabi*",
    ]

@subpackage("libllvm")
def _libllvm(self):
    self.short_desc = short_desc + " - runtime library"

    return [f"usr/lib/libLLVM-{_mver}.so"]

@subpackage("lld")
def _lld(self):
    self.short_desc = short_desc + " - linker"

    return [
        "usr/bin/ld",
        "usr/bin/lld*",
        "usr/bin/wasm-ld",
        "usr/bin/ld.lld*",
        "usr/bin/ld64.lld*"
    ]

@subpackage("lld-devel")
def _lld_devel(self):
    self.short_desc = short_desc + " - linker - development files"
    self.depends = [f"lld={version}-r{revision}"]

    return [
        "usr/include/lld",
        "usr/lib/cmake/lld",
        "usr/lib/liblld*a"
    ]

@subpackage("llvm-linker-tools")
def _llvm_linker_tools(self):
    self.short_desc = short_desc + " - linker plugins"

    return [
        "usr/lib/libLTO.so.*"
    ]

@subpackage("llvm-devel")
def _llvm_devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [
        f"llvm={version}-r{revision}",
        f"llvm-tools={version}-r{revision}",
        f"libclang-cpp={version}-r{revision}"
    ]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/cmake",
    ]

@subpackage("llvm-tools")
def _llvm_tools(self):
    self.short_desc = short_desc + " - testing tools"

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
    self.short_desc = short_desc + " - runtime"

    return [
        "usr/bin/lli*",
    ]
