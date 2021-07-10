pkgname = "clang-rt-cross-base"
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
hostmakedepends = ["cmake", "gmake", "python", "llvm", "clang-tools-extra"]
makedepends = ["zlib-devel", "libffi-devel"]
depends = []
make_cmd = "make"
short_desc = "Low Level Virtual Machine (aarch64 core runtime)"
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

cmake_dir = "compiler-rt"

CFLAGS = ["-O2", "-fPIC"]

subpackages = []

_triplets = [
    ("aarch64", "aarch64-linux-musl", ["-march=armv8-a"]),
    ("ppc64le", "powerpc64le-linux-musl", ["-mtune=power9"]),
    ("x86_64", "x86_64-linux-musl", []),
]

from cbuild.util import cmake, make
from cbuild import cpu

def post_patch(self):
    import shutil
    shutil.move(
        self.builddir / f"musl-{_musl_version}", self.abs_wrksrc / "musl"
    )

def init_configure(self):
    self.make = make.Make(self)

def do_configure(self):
    for an, at, cflags in _triplets:
        if cpu.target() == an:
            continue

        self.CFLAGS = CFLAGS + cflags
        # musl build dir
        mbpath = self.abs_wrksrc / f"musl/build-{an}"
        mbpath.mkdir(exist_ok = True)
        # configure musl
        if not (mbpath / ".configure_done").exists():
            self.do(
                self.chroot_wrksrc / "musl/configure",
                ["--prefix=/usr", "--host=" + at], build = True,
                wrksrc = self.chroot_wrksrc / f"musl/build-{an}",
                env = {
                    "CC": "clang -target " + at
                }
            )
            (mbpath / ".configure_done").touch()
        # install musl headers for arch
        if not (mbpath / ".install_done").exists():
            make.Make(
                self, command = "gmake",
                wrksrc = self.chroot_wrksrc / f"musl/build-{an}"
            ).invoke(
                "install-headers",
                ["DESTDIR=" + str(self.chroot_wrksrc / f"musl-{an}")]
            )
            (mbpath / ".install_done").touch()
        # configure compiler-rt
        cbpath = self.abs_wrksrc / f"build-{an}"
        if not (cbpath / ".configure_done").exists():
            cmake.configure(self, self.cmake_dir, f"build-{an}", [
                "-DCMAKE_SYSROOT=" + str(self.chroot_wrksrc  / f"musl-{an}"),
                f"-DCMAKE_ASM_COMPILER_TARGET={at}",
                f"-DCMAKE_C_COMPILER_TARGET={at}"
            ])
            (cbpath / ".configure_done").touch()

def do_build(self):
    for an, at, cflags in _triplets:
        if cpu.target() == an:
            continue

        cbpath = self.abs_wrksrc / f"build-{an}"
        if not (cbpath / ".build_done").exists():
            self.make.build(wrksrc = f"build-{an}")
            (cbpath / ".build_done").touch()

def do_install(self):
    for an, at, cflags in _triplets:
        if cpu.target() == an:
            continue
        self.make.install(wrksrc = f"build-{an}")

def _gen_subp(an, at):
    def _subp(self):
        self.short_desc = f"{short_desc} - {an} support"
        self.depends = [f"clang>={version}"]
        return [f"usr/lib/clang/{version}/lib/linux/*{at[0:at.find('-')]}*"]

    return _subp

for an, at, cflags in _triplets:
    if cpu.target() == an:
        continue

    subpackages.append((f"clang-rt-cross-base-{an}", _gen_subp(an, at)))
    depends.append(f"clang-rt-cross-base-{an}={version}-r{revision}")
