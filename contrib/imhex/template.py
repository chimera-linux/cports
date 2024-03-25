pkgname = "imhex"
pkgver = "1.33.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DIMHEX_BUNDLE_DOTNET=OFF",
    "-DIMHEX_DISABLE_STACKTRACE=ON",
    "-DIMHEX_ENABLE_UNIT_TESTS=ON",
    "-DIMHEX_IGNORE_BAD_CLONE=ON",
    "-DIMHEX_OFFLINE_BUILD=YES",
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
source = f"https://github.com/WerWolv/ImHex/releases/download/v{pkgver}/Full.Sources.tar.gz"
sha256 = "c126ecebb639f68050a47d1f9ea0e060c6ae25bfade87237cb54f2e584cfa252"


@subpackage("imhex-devel")
def _devel(self):
    return ["usr/share/imhex/sdk"]
