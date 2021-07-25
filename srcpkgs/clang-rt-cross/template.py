pkgname = "clang-rt-cross"
version = "12.0.0"
revision = 0
wrksrc = f"llvm-project-{version}.src"
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{version}",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=YES",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_CXX_COMPILER=/usr/bin/clang++",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
    # skip builtins since those are already provided by -base
    "-DCOMPILER_RT_BUILD_BUILTINS=OFF",
    "-DCOMPILER_RT_BUILD_CRT=OFF",
    # we need these as an intermediate copy of libcxx is built in the process
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=YES",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
]
hostmakedepends = [
    "cmake", "gmake", "python", "llvm-devel", "clang-tools-extra"
]
makedepends = [
    "zlib-devel", "libffi-devel", "clang-rt-cross-base",
    "libcxx-cross", "libexecinfo-cross", "kernel-libc-headers-cross"
]
depends = ["clang-rt-cross-base", "libcxx-cross", "libexecinfo-cross"]
make_cmd = "make"
short_desc = "Cross-compiling runtime for LLVM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://llvm.org"
distfiles = [
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz"
]
checksum = [
    "9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628"
]
nocross = True

cmake_dir = "compiler-rt"

CFLAGS = ["-fPIC"]
CXXFLAGS = ["-fPIC"]

_targets = list(filter(
    lambda p: p != current.build_profile.arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

from cbuild.util import cmake, make

def init_configure(self):
    self.make = make.Make(self)

def do_configure(self):
    for an in _targets:
        with self.profile(an):
            at = self.build_profile.short_triplet
            # configure compiler-rt
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(self, self.cmake_dir, f"build-{an}", [
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}"
                ])

def do_build(self):
    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc = f"build-{an}")

def do_install(self):
    import shutil

    for an in _targets:
        with self.profile(an):
            self.make.install(wrksrc = f"build-{an}")

    # we don't need or want these for cross
    shutil.rmtree(self.destdir / f"usr/lib/clang/{version}/share")
    shutil.rmtree(self.destdir / f"usr/lib/clang/{version}/include")
    shutil.rmtree(self.destdir / f"usr/lib/clang/{version}/bin")

def _gen_crossp(an):
    with current.profile(an):
        at = current.build_profile.short_triplet

    @subpackage(f"clang-rt-cross-{an}")
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [
            f"clang-rt-cross-base-{an}",
            f"libcxx-cross-{an}",
            f"libexecinfo-cross-{an}"
        ]
        self.options = ["!scanshlibs"]
        return [f"usr/lib/clang/{version}/lib/linux/libclang_rt.*{at[0:at.find('-')]}*"]
    depends.append(f"clang-rt-cross-{an}={version}-r{revision}")

for an in _targets:
    _gen_crossp(an)
