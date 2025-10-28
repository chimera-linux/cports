pkgname = "clang-rt-cross"
pkgver = "21.1.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0 : pkgver.find('.')]}",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=ON",
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
    "-DLIBCXX_USE_COMPILER_RT=ON",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=ON",
    "-DLIBCXX_HAS_MUSL_LIBC=ON",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=ON",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=ON",
    "-DLIBCXXABI_USE_COMPILER_RT=ON",
    # use multiarch style paths
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
]
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "llvm-devel",
    "ninja",
    "python",
]
makedepends = [
    "clang-rt-crt-cross",
    "libffi8-devel",
    "linux-headers-cross",
    "llvm-runtimes-cross",
    "zlib-ng-compat-devel",
]
depends = ["clang-rt-crt-cross", "llvm-runtimes-cross"]
pkgdesc = "Cross-compiling runtime for LLVM"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "a01ad7e5167780c945871d75c0413081d12067607a6de5cf71dc3e8d1a82112c"
# crosstoolchain
options = ["!cross", "!check", "!lto", "empty"]

cmake_dir = "compiler-rt"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

_targetlist = [
    "aarch64",
    "armhf",
    "armv7",
    "ppc64le",
    "ppc64",
    "ppc",
    "x86_64",
    "riscv64",
    "loongarch64",
]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))


def configure(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # configure compiler-rt
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(
                    self,
                    f"build-{an}",
                    self.cmake_dir,
                    [
                        *configure_args,
                        f"-DCMAKE_SYSROOT=/usr/{at}",
                        f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                        f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                        f"-DCMAKE_C_COMPILER_TARGET={at}",
                    ],
                    cross_build=False,
                )


def build(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an):
            with self.stamp(f"{an}_build") as s:
                s.check()
                cmake.build(self, f"build-{an}")


def install(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an):
            cmake.install(self, f"build-{an}")

    self.install_license("LICENSE.TXT")

    # we don't need or want these for cross
    with self.pushd(self.destdir):
        self.rm(
            f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/share",
            recursive=True,
        )
        self.rm(
            f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/include",
            recursive=True,
        )
        self.rm(
            f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/bin", recursive=True
        )


def _gen_subp(an):
    @subpackage(f"clang-rt-cross-{an}", an in _targets)
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = [
            f"clang-rt-crt-cross-{an}",
            f"llvm-runtimes-cross-{an}",
        ]
        self.options = [
            "!scanshlibs",
            "!scanrundeps",
            "!splitstatic",
            "foreignelf",
        ]
        with self.rparent.profile(an) as pf:
            return [
                f"usr/lib/clang/{pkgver[0 : pkgver.find('.')]}/lib/{pf.triplet}"
            ]

    if an in _targets:
        depends.append(self.with_pkgver(f"clang-rt-cross-{an}"))


for _an in _targetlist:
    _gen_subp(_an)
