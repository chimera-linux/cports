pkgname = "android-tools"
pkgver = "35.0.1"
pkgrel = 2
# only supports specific little-endian archs, particularly in boringssl
archs = ["x86_64", "aarch64", "ppc64le", "riscv64"]
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
    "gtest-devel",
    "libusb-devel",
    "linux-headers",
    "lz4-devel",
    "pcre2-devel",
    "protobuf-devel",
    "zstd-devel",
]
depends = ["android-udev-rules", "python"]
pkgdesc = "Android platform tools (e.g. adb and fastboot)"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0 AND ISC AND GPL-2.0-only AND MIT"
url = "https://github.com/nmeum/android-tools"
source = f"{url}/releases/download/{pkgver}/android-tools-{pkgver}.tar.xz"
sha256 = "654030c7f96d25d7224cd6861fac14a043cf1d3980f40288cdfbe219f94ffaf9"
tool_flags = {"CXXFLAGS": ["-D_LARGEFILE64_SOURCE"]}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("vendor/boringssl/LICENSE", name="boringssl.LICENSE")
    self.install_license(
        "vendor/boringssl/third_party/fiat/LICENSE", name="fiat.LICENSE"
    )
