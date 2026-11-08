pkgname = "zig"
pkgver = "0.17.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # dodge -Dstrip
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DZIG_PIE=ON",
    "-DZIG_SHARED_LLVM=ON",
    "-DZIG_TARGET_MCPU=baseline",
    # langref doctests compile native examples without an explicit target
    "-DZIG_EXTRA_BUILD_ARGS=-Dno-langref",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "clang-devel",
    "linux-headers",
    "lld-devel",
    "llvm-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Zig programming language toolchain"
license = "MIT"
url = "https://github.com/ziglang/zig"
source = f"https://ziglang.org/download/{pkgver}/zig-{pkgver}.tar.xz"
sha256 = "1e89bf06610b769a8c77676c6c8d54b093a0db60f4891f2f91014829012f0e24"
# lighten up the build, only applies to bootstrap and just slows down the build
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE"]}
hardening = ["!int", "!scp", "!ssp", "!var-init"]
# the test suite's configure step fails in the offline cbuild sandbox
options = ["!lto", "!check"]

restricted = "work in progress (needs to either not need llvm or for us to multiversion llvm)"

# Chimera's clang uses compiler-rt rather than GCC's crtbegin/crtend, which
# Zig's native libc detection cannot handle. Build the compiler for the musl
# target explicitly so it uses the bundled libc instead. Users must likewise
# pass -Dtarget=<arch>-linux-musl when compiling native code.
_zig_targets = {
    "x86_64": "x86_64-linux-musl",
    "aarch64": "aarch64-linux-musl",
    "ppc64le": "powerpc64le-linux-musl",
    "ppc64": "powerpc64-linux-musl",
    "ppc": "powerpc-linux-musl",
    "riscv64": "riscv64-linux-musl",
    "loongarch64": "loongarch64-linux-musl",
    "armv7": "arm-linux-musleabihf",
    "armhf": "arm-linux-musleabihf",
}
_zig_target = _zig_targets.get(self.profile.arch)
if _zig_target is None:
    broken = f"unknown zig target for {self.profile.arch}"
else:
    configure_args += [
        "-DZIG_USE_LLVM_CONFIG=ON",
        f"-DZIG_TARGET_TRIPLE={_zig_target}",
    ]

def check(self):
    self.do(
        self.make_dir + "/stage3/bin/zig",
        "build",
        "test",
        "--summary",
        "all",
        f"-Dtarget={_zig_target}",
        "-Dcpu=baseline",
        "-Dskip-debug",
        "-Dskip-non-native",
        "-Dskip-release-safe",
        "-Dskip-release-small",
    )


def install(self):
    self.install_license("LICENSE")
    self.install_files(f"{self.make_dir}/stage3/bin", "usr")
    self.install_files(f"{self.make_dir}/stage3/lib", "usr")
