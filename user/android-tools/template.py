pkgname = "android-tools"
pkgver = "35.0.2"
pkgrel = 23
# only supports specific little-endian archs, particularly in boringssl
archs = ["x86_64", "aarch64", "ppc64le", "riscv64"]
build_style = "cmake"
configure_args = [
    # until next libusb
    "-DANDROID_TOOLS_USE_BUNDLED_LIBUSB=ON",
    "-DANDROID_TOOLS_LIBUSB_ENABLE_UDEV=ON",
]
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
    "udev-devel",
    "zstd-devel",
]
depends = ["android-udev-rules", "python"]
pkgdesc = "Android platform tools, such as adb and fastboot"
license = "Apache-2.0 AND ISC AND GPL-2.0-only AND MIT"
url = "https://github.com/nmeum/android-tools"
source = f"{url}/releases/download/{pkgver}/android-tools-{pkgver}.tar.xz"
sha256 = "d2c3222280315f36d8bfa5c02d7632b47e365bfe2e77e99a3564fb6576f04097"
tool_flags = {"CXXFLAGS": ["-D_LARGEFILE64_SOURCE"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("vendor/boringssl/LICENSE", name="boringssl.LICENSE")
    self.install_license(
        "vendor/boringssl/third_party/fiat/LICENSE", name="fiat.LICENSE"
    )
