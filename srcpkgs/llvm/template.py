pkgname = "llvm"
version = "12.0.0"
revision = 1
wrksrc = f"llvm-project-{version}.src"
build_style = "cmake"
configure_args = [
    # don't enable lldb for now, we don't package enough for it
    "-DLLVM_ENABLE_PROJECTS=clang;clang-tools-extra;compiler-rt;libcxx;libcxxabi;libunwind;lld;openmp",
    # other stuff
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
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
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "perl", "python", "zlib-devel", "libffi-devel"
]
makedepends = [
    "python-devel", "zlib-devel", "libffi-devel", "libedit-devel",
    "libexecinfo-devel"
]
depends = [
    f"libllvm={version}-r{revision}",
    f"libomp={version}-r{revision}",
    "libexecinfo-devel"
]
short_desc = "Low Level Virtual Machine"
maintainer = "q66 <daniel@octaforge.org>"
license = "Apache-2.0"
homepage = "https://llvm.org"
distfiles = [f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz"]
checksum = ["9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628"]

cmake_dir = "llvm"

def pre_configure(self):
    from cbuild import cpu

    larch = cpu.match_target(
        "x86_64*", "X86",
        "ppc*", "PowerPC",
        "aarch64*", "AArch64"
    )

    self.configure_args.append("-DLLVM_TARGET_ARCH=" + larch)
    self.configure_args.append("-DLLVM_HOST_TRIPLE=" + self.triplet)
    self.configure_args.append("-DLLVM_DEFAULT_TARGET_TRIPLE=" + self.triplet)

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

    return [
        "usr/lib/libomp.so",
        #"usr/lib/libomptarget.rtl.*.so", FIXME need libelf
        "usr/lib/libarcher.so",
        "usr/lib/libomp*.so.*"
    ]

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
        "musl-devel",
    ]

    return [
        "usr/include/clang",
        "usr/include/clang-c",
        "usr/bin/*clang*",
        "usr/bin/c-index-test",
        "usr/lib/clang",
        "usr/lib/cmake/clang",
        "usr/lib/libclang*.a",
        "usr/lib/libclang*.so",
        "usr/share/clang"
    ]

@subpackage("clang-analyzer")
def _clang_analyzer(self):
    self.short_desc = short_desc + " - Source code analysis"
    self.depends = [
        f"clang={version}-r{revision}",
        f"python",
    ]

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

    return ["usr/lib/libLLVM-*.so*"]

@subpackage("lld")
def _lld(self):
    self.short_desc = short_desc + " - linker"

    return [
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
