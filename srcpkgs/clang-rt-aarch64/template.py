pkgname = "clang-rt-aarch64"
archs = "~aarch64"
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
    # triplets
    "-DCMAKE_ASM_COMPILER_TARGET=aarch64-linux-musl",
    "-DCMAKE_C_COMPILER_TARGET=aarch64-linux-musl",
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
depends = [f"clang>={version}"]
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

CFLAGS = ["-fPIC", "-march=armv8-a"]

def post_patch(self):
    import shutil
    shutil.move(
        self.builddir / f"musl-{_musl_version}", self.abs_wrksrc / "musl"
    )

def pre_configure(self):
    from cbuild.util import make
    (self.abs_wrksrc / "musl/build").mkdir()
    # configure musl for headers
    self.do(
        self.chroot_wrksrc / "musl/configure",
        ["--prefix=/usr"], build = True,
        wrksrc = self.chroot_wrksrc / "musl/build"
    )
    make.Make(
        self, command = "gmake", wrksrc = self.chroot_wrksrc / "musl/build"
    ).invoke(
        "install-headers", ["DESTDIR=" + str(self.chroot_wrksrc / "musl-root")]
    )
    self.configure_args.append(
        "-DCMAKE_SYSROOT=" + str(self.chroot_wrksrc / "musl-root")
    )
    # do not use any of the host-specific cflags for the target build
    self.CFLAGS = CFLAGS
