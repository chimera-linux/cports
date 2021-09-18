pkgname = "clang-rt-crt-cross"
_musl_version = "1.2.2"
version = "12.0.0"
revision = 0
wrksrc = f"llvm-project-{version}.src"
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    f"-DCMAKE_INSTALL_PREFIX=/usr/lib/clang/{version}",
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
]
hostmakedepends = [
    "cmake", "gmake", "python", "llvm-devel", "clang-tools-extra"
]
makedepends = ["zlib-devel", "libffi-devel"]
depends = []
make_cmd = "make"
short_desc = "Core cross-compiling runtime for LLVM"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://llvm.org"
distfiles = [
    f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{version}/llvm-project-{version}.src.tar.xz",
    f"http://www.musl-libc.org/releases/musl-{_musl_version}.tar.gz"
]
checksum = [
    "9ed1688943a4402d7c904cc4515798cdb20080066efa010fe7e1f2551b423628",
    "9b969322012d796dc23dda27a35866034fa67d8fb67e0e2c45c913c3d43219dd"
]
options = ["!cross", "!check"]

cmake_dir = "compiler-rt"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

subpackages = []

_targets = list(filter(
    lambda p: p != current.build_profile.arch,
    ["aarch64", "ppc64le", "ppc64", "x86_64", "riscv64"]
))

def post_patch(self):
    self.mv(self.builddir / f"musl-{_musl_version}", "musl")

def do_configure(self):
    from cbuild.util import cmake, make

    for an in _targets:
        with self.profile(an):
            at = self.build_profile.short_triplet
            # musl build dir
            self.mkdir(f"musl/build-{an}", parents = True)
            # configure musl
            with self.stamp(f"{an}_musl_configure") as s:
                s.check()
                self.do(
                    self.chroot_cwd / "musl/configure",
                    ["--prefix=/usr", "--host=" + at],
                    wrksrc = f"musl/build-{an}",
                    env = {
                        "CC": "clang -target " + at
                    }
                )
            # install musl headers for arch
            with self.stamp(f"{an}_musl_install") as s:
                s.check()
                make.Make(
                    self, command = "gmake",
                    wrksrc = self.chroot_cwd / f"musl/build-{an}"
                ).invoke(
                    "install-headers",
                    ["DESTDIR=" + str(self.chroot_cwd / f"musl-{an}")]
                )
            # configure compiler-rt
            with self.stamp(f"{an}_configure") as s:
                s.check()
                cmake.configure(self, self.cmake_dir, f"build-{an}", [
                    "-DCMAKE_SYSROOT=" + str(self.chroot_cwd  / f"musl-{an}"),
                    f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                    f"-DCMAKE_C_COMPILER_TARGET={at}",
                    f"-DCMAKE_CXX_COMPILER_TARGET={at}",
                    # override the cflags-provided sysroot
                    f"-DCMAKE_C_FLAGS=" + self.get_cflags([
                        "--sysroot=" + str(self.chroot_cwd  / f"musl-{an}")
                    ], shell = True)
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

def _gen_subp(an, at):
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [f"clang>={version}"]
        return [f"usr/lib/clang/{version}/lib/linux/*{at[0:at.find('-')]}*"]

    return _subp

for an in _targets:
    with current.profile(an):
        at = current.build_profile.short_triplet

    subpackages.append((f"clang-rt-crt-cross-{an}", _gen_subp(an, at)))
    depends.append(f"clang-rt-crt-cross-{an}={version}-r{revision}")
