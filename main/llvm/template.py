pkgname = "llvm"
_mver = "12"
pkgver = f"{_mver}.0.0"
pkgrel = 0
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
hostmakedepends = [
    "cmake", "pkgconf", "perl", "python", "zlib-devel", "libffi-devel"
]
makedepends = ["zlib-devel", "libffi-devel"]
depends = [
    f"libllvm={pkgver}-r{pkgrel}",
    f"libomp={pkgver}-r{pkgrel}",
    f"llvm-linker-tools={pkgver}-r{pkgrel}",
    f"llvm-runtime={pkgver}-r{pkgrel}"
]
make_cmd = "make"
pkgdesc = "Low Level Virtual Machine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628"

options = ["bootstrap", "!check", "!lint"]

cmake_dir = "llvm"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

if not current.bootstrapping:
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

match current.profile().arch:
    case "x86_64": _arch = "X86"
    case "aarch64": _arch = "AArch64"
    case "ppc64le" | "ppc64": _arch = "PowerPC"
    case "riscv64": _arch = "RISCV64"
    case _:
        broken = f"Unknown CPU architecture: {current.profile().arch}"

def init_configure(self):
    if not self.cross_build:
        return

    self.configure_args.append("-DLLVM_TABLEGEN=" + str(self.chroot_cwd / "build_host/bin/llvm-tblgen"))
    self.configure_args.append("-DCLANG_TABLEGEN=" + str(self.chroot_cwd / "build_host/bin/clang-tblgen"))

def pre_configure(self):
    if not self.cross_build:
        return

    from cbuild.util import make, cmake

    self.log("building host tblgen...")

    with self.profile("host"):
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

    # when bootstrapping, this will check the actual profile
    with self.profile(self.profile().arch) as pf:
        trip = pf.short_triplet

    cmake.configure(self, self.cmake_dir, "build", [
        "-DLLVM_TARGET_ARCH=" + _arch,
        "-DLLVM_HOST_TRIPLE=" + trip,
        "-DLLVM_DEFAULT_TARGET_TRIPLE=" + trip,
    ])

def post_install(self):
    self.install_file(
        "libcxxabi/include/__cxxabi_config.h", "usr/include"
    )
    self.install_file(
        "libcxxabi/include/cxxabi.h", "usr/include"
    )

    self.install_dir("usr/include/mach-o")
    self.install_file(
        "libunwind/include/__libunwind_config.h", "usr/include"
    )
    self.install_file(
        "libunwind/include/libunwind.h", "usr/include"
    )
    self.install_file(
        "libunwind/include/unwind.h", "usr/include"
    )
    self.install_file(
        "libunwind/include/mach-o/compact_unwind_encoding.h",
        "usr/include/mach-o"
    )
    # it's our default toolchain
    self.install_link("clang", "usr/bin/cc")
    self.install_link("clang++", "usr/bin/c++")
    if not (self.destdir / "usr/bin/ld").is_symlink():
        self.install_link("ld.lld", "usr/bin/ld")

@subpackage("clang-tools-extra")
def _tools_extra(self):
    self.pkgdesc = f"{pkgdesc} (extra Clang tools)"
    self.depends = [f"clang={pkgver}-r{pkgrel}"]

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
    self.pkgdesc = f"{pkgdesc} (Clang OpenMP support library)"

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
    self.pkgdesc = f"{pkgdesc} (Clang OpenMP support library) (development files)"
    self.depends = [f"libomp={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/libomp*.so",
        "usr/lib/libarcher*",
        "usr/include/omp*.h",
        f"usr/lib/clang/{pkgver}/include/omp*.h"
    ]

@subpackage("clang")
def _clang(self):
    self.pkgdesc = f"{pkgdesc} (C language family frontend)"
    self.depends = [
        f"libcxx-devel={pkgver}-r{pkgrel}",
        f"libcxxabi-devel={pkgver}-r{pkgrel}",
        f"clang-rt-devel={pkgver}-r{pkgrel}",
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
    self.pkgdesc = f"{pkgdesc} (Clang runtime development files)"

    return [
        "usr/lib/clang"
    ]

@subpackage("clang-devel")
def _clang_devel(self):
    self.pkgdesc = f"{pkgdesc} (Clang development files)"
    self.depends = [
        f"clang-rt-devel={pkgver}-r{pkgrel}",
        f"libclang={pkgver}-r{pkgrel}",
        f"libclang-cpp={pkgver}-r{pkgrel}",
        f"libcxx-devel={pkgver}-r{pkgrel}"
    ]

    return [
        "usr/include/clang",
        "usr/include/clang-c",
        "usr/lib/libclang*.a",
        "usr/lib/libclang*.so",
    ]

@subpackage("clang-analyzer")
def _clang_analyzer(self):
    self.pkgdesc = f"{pkgdesc} (source code analysis)"
    self.depends = [f"clang={pkgver}-r{pkgrel}"]
    if not self.bootstrapping:
        self.depends.append("python")

    return [
        "usr/bin/scan-*",
        "usr/share/scan-*",
        "usr/libexec/*analyzer",
    ]

@subpackage("libclang")
def _libclang(self):
    self.pkgdesc = f"{pkgdesc} (C frontend runtime library)"

    return ["usr/lib/libclang.so.*"]

@subpackage("libclang-cpp")
def _libclang_cpp(self):
    self.pkgdesc = f"{pkgdesc} (C frontend runtime library)"

    return ["usr/lib/libclang-cpp.so.*"]

@subpackage("libunwind")
def _libunwind(self):
    self.pkgdesc = f"{pkgdesc} (libunwind)"

    return ["usr/lib/libunwind.so.*"]

@subpackage("libunwind-devel")
def _libunwind_devel(self):
    self.pkgdesc = f"{pkgdesc} (libunwind) (development files)"
    self.depends = [f"libunwind={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/libunwind.so",
        "usr/lib/libunwind.a",
        "usr/include/*unwind*",
        "usr/include/mach-o"
    ]

@subpackage("libcxx")
def _libcxx(self):
    self.pkgdesc = f"{pkgdesc} (C++ standard library)"

    return ["usr/lib/libc++.so.*"]

@subpackage("libcxx-devel")
def _libcxx_devel(self):
    self.pkgdesc = f"{pkgdesc} (C++ standard library) (development files)"
    self.depends = [f"libcxx={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/libc++.so",
        "usr/lib/libc++.a",
        "usr/lib/libc++experimental.a",
        "usr/include/c++",
    ]

@subpackage("libcxxabi")
def _libcxxabi(self):
    self.pkgdesc = f"{pkgdesc} (low level C++ runtime)"
    self.depends = [f"libunwind={pkgver}-r{pkgrel}"]

    return ["usr/lib/libc++abi.so.*"]

@subpackage("libcxxabi-devel")
def _libcxxabi_devel(self):
    self.pkgdesc = f"{pkgdesc} (low level C++ runtime) (development files)"
    self.depends = [
        f"libcxxabi={pkgver}-r{pkgrel}",
        f"libunwind-devel={pkgver}-r{pkgrel}"
    ]

    return [
        "usr/lib/libc++abi.so",
        "usr/lib/libc++abi.a",
        "usr/include/*cxxabi*",
    ]

@subpackage("libllvm")
def _libllvm(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return [f"usr/lib/libLLVM-{_mver}.so"]

@subpackage("lld")
def _lld(self):
    self.pkgdesc = f"{pkgdesc} (linker)"

    return [
        "usr/bin/ld",
        "usr/bin/lld*",
        "usr/bin/wasm-ld",
        "usr/bin/ld.lld*",
        "usr/bin/ld64.lld*"
    ]

@subpackage("lld-devel")
def _lld_devel(self):
    self.pkgdesc = f"{pkgdesc} (linker) (development files)"
    self.depends = [f"lld={pkgver}-r{pkgrel}"]

    return [
        "usr/include/lld",
        "usr/lib/cmake/lld",
        "usr/lib/liblld*a"
    ]

@subpackage("llvm-linker-tools")
def _llvm_linker_tools(self):
    self.pkgdesc = f"{pkgdesc} (linker plugins)"

    return [
        "usr/lib/libLTO.so.*"
    ]

@subpackage("llvm-devel")
def _llvm_devel(self):
    self.depends = [
        f"llvm={pkgver}-r{pkgrel}",
        f"llvm-tools={pkgver}-r{pkgrel}",
        f"libclang-cpp={pkgver}-r{pkgrel}"
    ]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
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
