pkgname = "imhex"
pkgver = "1.35.2"
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
_patterns = "a0bb71be5864588fd0f33ec524c8a3b32dcc3a59"
source = [
    f"https://github.com/WerWolv/ImHex/releases/download/v{pkgver}/Full.Sources.tar.gz>src-{pkgver}.tar.gz",
    f"https://github.com/WerWolv/ImHex-Patterns/archive/{_patterns}.tar.gz",
]
source_paths = [".", "ImHex-Patterns"]
sha256 = [
    "8296449547b8b446b352907144bbd02f1abefa7ba1af6311c7490d8f8f883e51",
    "895aea1e0f4367f0e52e25205c459bbe8589d2f094d676e0874982a7ca5ae359",
]


@subpackage("imhex-devel")
def _devel(self):
    return ["usr/share/imhex/sdk"]
