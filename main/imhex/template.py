pkgname = "imhex"
pkgver = "1.36.0"
pkgrel = 0
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
    "curl-devel",
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
_plutovg_ver = "0.0.10"
source = [
    f"https://github.com/WerWolv/ImHex/releases/download/v{pkgver}/Full.Sources.tar.gz>src-{pkgver}.tar.gz",
    f"https://github.com/WerWolv/ImHex-Patterns/archive/refs/tags/ImHex-v{pkgver}.tar.gz",
    f"https://github.com/sammycage/plutovg/archive/refs/tags/v{_plutovg_ver}.tar.gz",
]
source_paths = [
    ".",
    "ImHex-Patterns",
    "build/_deps/plutovg-src",
]
sha256 = [
    "ee464053969ae5f5754ebb1afb3bbdcf2faa4ac195fad0f7ff43cf129abcab04",
    "a2a3820037c2ca23fa834526ee605bf166fba910f43a08089b9037e1e87d3609",
    "639ce28e8f12920ed19d96cd50809973ded904a4e17ba7f9986d6e88431e93c6",
]


def post_install(self):
    self.uninstall("usr/bin/imhex-updater")


@subpackage("imhex-devel")
def _(self):
    return self.default_devel(extra=["usr/share/imhex/sdk"])
