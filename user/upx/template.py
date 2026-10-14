pkgname = "upx"
pkgver = "5.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DUPX_CONFIG_DISABLE_WERROR=ON",
    "-DUPX_CONFIG_DISABLE_SANITIZE=ON",
    "-DUPX_CONFIG_DISABLE_GITREV=ON",
]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Advanced executable file compressor"
license = "GPL-2.0-or-later"
url = "https://upx.github.io"
source = [
    f"https://github.com/upx/upx/releases/download/v{pkgver}/upx-{pkgver}-src.tar.xz"
]
sha256 = [
    "a7d457be4ef942e46844ee8f301206b111394cbcbde3599747a6904c54ff116b",
]
hardening = ["vis", "cfi"]
