pkgname = "android-tools"
pkgver = "36.0.1"
pkgrel = 0
# only supports specific little-endian archs, particularly in boringssl
archs = ["x86_64", "aarch64", "loongarch64", "ppc64le", "riscv64"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "go",
    "ninja",
    "perl",
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
sha256 = "38e8a84b739480141de0836bf6d581b3339ac7d53d0f7ce8c044a3368c8c2f8f"
tool_flags = {"CXXFLAGS": ["-D_LARGEFILE64_SOURCE"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("vendor/boringssl/LICENSE", name="boringssl.LICENSE")
    self.install_license(
        "vendor/boringssl/third_party/fiat/LICENSE", name="fiat.LICENSE"
    )
