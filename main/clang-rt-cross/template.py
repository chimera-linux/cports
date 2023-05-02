pkgname = "clang-rt-cross"
pkgver = "16.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0:pkgver.find('.')]}",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=YES",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # disable execinfo
    "-DCOMPILER_RT_BUILD_GWP_ASAN=OFF",
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
    # use multiarch style paths
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=YES",
]
make_cmd = "make"
hostmakedepends = [
    "cmake", "gmake", "python", "llvm-devel", "clang-tools-extra"
]
makedepends = [
    "zlib-devel", "libffi-devel", "clang-rt-crt-cross",
    "libcxx-cross", "linux-headers-cross"
]
depends = ["clang-rt-crt-cross", "libcxx-cross"]
pkgdesc = "Cross-compiling runtime for LLVM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "6d8acae041ccd34abe144cda6eaa76210e1491f286574815b7261b3f2e58734c"
# crosstoolchain
options = ["!cross", "!check", "!lto"]

cmake_dir = "compiler-rt"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

_targetlist = ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))

def do_configure(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # configure compiler-rt
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(self, self.cmake_dir, f"build-{an}", [
                    f"-DCMAKE_SYSROOT=/usr/{at}",
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}"
                ], cross_build = False)

def do_build(self):
    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                self.make.build(wrksrc = f"build-{an}")

def do_install(self):
    for an in _targets:
        with self.profile(an):
            self.make.install(wrksrc = f"build-{an}")

    # we don't need or want these for cross
    with self.pushd(self.destdir):
        self.rm(f"usr/lib/clang/{pkgver[0:pkgver.find('.')]}/share", recursive = True)
        self.rm(f"usr/lib/clang/{pkgver[0:pkgver.find('.')]}/include", recursive = True)
        self.rm(f"usr/lib/clang/{pkgver[0:pkgver.find('.')]}/bin", recursive = True)

def _gen_subp(an):
    @subpackage(f"clang-rt-cross-{an}", an in _targets)
    def _subp(self):
        self.pkgdesc = f"{pkgdesc} ({an} support)"
        self.depends = [
            f"clang-rt-crt-cross-{an}",
            f"libcxx-cross-{an}",
        ]
        self.options = [
            "!scanshlibs", "!scanrundeps", "!splitstatic", "foreignelf"
        ]
        with self.rparent.profile(an) as pf:
            return [f"usr/lib/clang/{pkgver[0:pkgver.find('.')]}/lib/{pf.triplet}"]

    if an in _targets:
        depends.append(f"clang-rt-cross-{an}={pkgver}-r{pkgrel}")


for an in _targetlist:
    _gen_subp(an)
