pkgname = "imhex"
pkgver = "1.35.4"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DIMHEX_BUNDLE_DOTNET=OFF",
    "-DIMHEX_DISABLE_STACKTRACE=ON",
    "-DIMHEX_ENABLE_UNIT_TESTS=ON",
    "-DIMHEX_IGNORE_BAD_CLONE=ON",
    "-DIMHEX_OFFLINE_BUILD=ON",
    "-DIMHEX_STRICT_WARNINGS=OFF",
    "-DIMHEX_STRIP_RELEASE=OFF",
    "-DUSE_SYSTEM_CAPSTONE=ON",
    "-DUSE_SYSTEM_FMT=ON",
    "-DUSE_SYSTEM_LLVM=ON",
    "-DUSE_SYSTEM_NLOHMANN_JSON=ON",
    "-DUSE_SYSTEM_YARA=ON",
]
make_build_args = ["--target", "all", "unit_tests"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "capstone-devel",
    # for llvm cmake detection to work
    "clang-tools-extra",
    "dbus-devel",
    "file-devel",
    "fmt-devel",
    "freetype-devel",
    "glfw-devel",
    "libarchive-devel",
    "libcurl-devel",
    "libedit-devel",
    "llvm-devel",
    # LLVMdemangle is static only
    "llvm-devel-static",
    "mbedtls-devel",
    "mesa-devel",
    "nlohmann-json",
    "xz-devel",
    "yara-devel",
]
pkgdesc = "Hex editor for reverse engineers"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://imhex.werwolv.net"
_patterns = "4299243e950bca438e16114937a2691ce23a4869"
source = [
    f"https://github.com/WerWolv/ImHex/releases/download/v{pkgver}/Full.Sources.tar.gz>src-{pkgver}.tar.gz",
    f"https://github.com/WerWolv/ImHex-Patterns/archive/{_patterns}.tar.gz",
]
source_paths = [".", "ImHex-Patterns"]
sha256 = [
    "987188df511a01dca407c4fd398a9dbc805ef82cdf044ea27da57ec343c7d6df",
    "ed187d7d143ecf0cb69bbb9186f7aea02fbd9bf996c7e55fc3893e73db45d7aa",
]


def post_install(self):
    self.uninstall("usr/bin/imhex-updater")


@subpackage("imhex-devel")
def _(self):
    return self.default_devel(extra=["usr/share/imhex/sdk"])
