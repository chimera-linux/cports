pkgname = "zig"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
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
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Zig programming language toolchain"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ziglang/zig"
source = f"https://ziglang.org/download/{pkgver}/zig-{pkgver}.tar.xz"
sha256 = "72014e700e50c0d3528cef3adf80b76b26ab27730133e8202716a187a799e951"
# the final output is zig3 built by zig2, C hardening only slows down the build
# or makes it fail without affecting the output
tool_flags = {
    "CFLAGS": ["-U_FORTIFY_SOURCE"],
    "CXXFLAGS": ["-U_FORTIFY_SOURCE"],
}
hardening = ["!int", "!scp", "!ssp", "!format", "!var-init"]
options = ["!lto"]


def do_check(self):
    self.do(
        self.make_dir + "/stage3/bin/zig",
        "build",
        "test",
        "--summary",
        "all",
        "-Dcpu=baseline",
        "-Dskip-cross-glibc",
        "-Dskip-debug",
        "-Dskip-non-native",
        "-Dskip-release-safe",
        "-Dskip-release-small",
    )


def post_install(self):
    self.install_license("LICENSE")
