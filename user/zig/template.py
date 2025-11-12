pkgname = "zig"
pkgver = "0.15.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # dodge -Dstrip
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DZIG_PIE=ON",
    "-DZIG_SHARED_LLVM=ON",
    "-DZIG_TARGET_MCPU=baseline",
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
sha256 = "d9b30c7aa983fcff5eed2084d54ae83eaafe7ff3a84d8fb754d854165a6e521c"
# lighten up the build, only applies to bootstrap and just slows down the build
tool_flags = {"CFLAGS": ["-U_FORTIFY_SOURCE"]}
hardening = ["!int", "!scp", "!ssp", "!var-init"]
options = ["!lto"]

restricted = "work in progress (needs to either not need llvm or for us to multiversion llvm)"

match self.profile().arch:
    case "x86_64" | "aarch64":
        pass
    case _:
        # disable tests on other archs, a lot of them fail
        options += ["!check"]


def check(self):
    self.do(
        self.make_dir + "/stage3/bin/zig",
        "build",
        "test",
        "--summary",
        "all",
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
