pkgname = "clang-rt-crt-cross"
_musl_ver = "1.2.5"
pkgver = "19.1.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{pkgver[0 : pkgver.find('.')]}",
    # prevent executable checks
    "-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY",
    # only build that target
    "-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON",
    # tools
    "-DCMAKE_C_COMPILER=/usr/bin/clang",
    "-DCMAKE_AR=/usr/bin/llvm-ar",
    "-DCMAKE_NM=/usr/bin/llvm-nm",
    "-DCMAKE_RANLIB=/usr/bin/llvm-ranlib",
    "-DLLVM_CONFIG_PATH=/usr/bin/llvm-config",
    # we are only building builtins and crt at this point
    "-DCOMPILER_RT_BUILD_BUILTINS=ON",
    "-DCOMPILER_RT_BUILD_CRT=ON",
    # disable everything else
    "-DCOMPILER_RT_BUILD_LIBFUZZER=OFF",
    "-DCOMPILER_RT_BUILD_MEMPROF=OFF",
    "-DCOMPILER_RT_BUILD_PROFILE=OFF",
    "-DCOMPILER_RT_BUILD_SANITIZERS=OFF",
    "-DCOMPILER_RT_BUILD_XRAY=OFF",
    "-DCOMPILER_RT_BUILD_ORC=OFF",
    "-DCOMPILER_RT_BUILD_CTX_PROFILE=OFF",
    # use multiarch style paths
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON",
]
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "ninja",
    "llvm-devel",
    "python",
]
makedepends = ["zlib-ng-compat-devel", "libffi-devel"]
depends = []
pkgdesc = "Core cross-compiling runtime for LLVM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = [
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz",
    f"https://www.musl-libc.org/releases/musl-{_musl_ver}.tar.gz",
]
source_paths = [".", "musl"]
sha256 = [
    "e3f79317adaa9196d2cfffe1c869d7c100b7540832bc44fe0d3f44a12861fa34",
    "a9a118bbe84d8764da0ea0d28b3ab3fae8477fc7e4085d90102b8596fc7c75e4",
]
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
]
_targets = sorted(filter(lambda p: p != self.profile().arch, _targetlist))


def configure(self):
    from cbuild.util import cmake

    for an in _targets:
        with self.profile(an) as pf:
            at = pf.triplet
            # musl build dir
            self.mkdir(f"musl/build-{an}", parents=True)
            # configure musl
            with self.stamp(f"{an}_musl_configure") as s:
                s.check()
                self.do(
                    self.chroot_cwd / "musl/configure",
                    "--prefix=/usr",
                    "--host=" + at,
                    wrksrc=f"musl/build-{an}",
                    env={"CC": "clang -target " + at},
                )
            # install musl headers for arch
            with self.stamp(f"{an}_musl_install") as s:
                s.check()
                self.do(
                    "make",
                    "-C",
                    f"musl/build-{an}",
                    "install-headers",
                    "DESTDIR=" + str(self.chroot_cwd / f"musl-{an}"),
                )
            # configure compiler-rt
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(
                    self,
                    f"build-{an}",
                    self.cmake_dir,
                    [
                        *configure_args,
                        "-DCMAKE_SYSROOT="
                        + str(self.chroot_cwd / f"musl-{an}"),
                        f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                        f"-DCMAKE_C_COMPILER_TARGET={at}",
                        f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                        # override the cflags-provided sysroot
                        "-DCMAKE_C_FLAGS="
                        + self.get_cflags(
                            [
                                "--sysroot="
                                + str(self.chroot_cwd / f"musl-{an}")
                            ],
                            shell=True,
                        ),
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


def _gen_subp(an):
    @subpackage(f"clang-rt-crt-cross-{an}", an in _targets)
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = ["clang"]
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
        depends.append(self.with_pkgver(f"clang-rt-crt-cross-{an}"))


for _an in _targetlist:
    _gen_subp(_an)
