pkgname = "android-tools"
pkgver = "37.0.0"
pkgrel = 0
# only supports specific little-endian archs, particularly in boringssl
archs = ["x86_64", "aarch64", "loongarch64", "ppc64le", "riscv64"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "protobuf",
]
makedepends = [
    "brotli-devel",
    "fmt-devel",
    "gtest-devel",
    "libusb-devel",
    "linux-headers",
    "lz4-devel",
    "pcre2-devel",
    "protobuf-devel",
    "zstd-devel",
]
depends = ["android-udev-rules", "python"]
pkgdesc = "Android platform tools, such as adb and fastboot"
license = "Apache-2.0 AND ISC AND GPL-2.0-only AND MIT"
url = "https://github.com/nmeum/android-tools"
source = f"{url}/releases/download/{pkgver}/android-tools-{pkgver}.tar.xz"
sha256 = "2725d09f892a3a38e534429f47a321f58ecf6a3169caa42c915fb2cb7d46be0e"
tool_flags = {"CXXFLAGS": ["-D_LARGEFILE64_SOURCE"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("vendor/boringssl/LICENSE", name="boringssl.LICENSE")
    self.install_license(
        "vendor/boringssl/third_party/fiat/LICENSE", name="fiat.LICENSE"
    )
