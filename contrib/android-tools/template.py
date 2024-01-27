pkgname = "android-tools"
pkgver = "34.0.4"
pkgrel = 3
# only supports specific little-endian archs, particularly in boringssl
archs = ["x86_64", "aarch64", "ppc64le", "riscv64"]
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "go", "pkgconf", "protobuf"]
makedepends = [
    "brotli-devel",
    "lz4-devel",
    "pcre2-devel",
    "libusb-devel",
    "zstd-devel",
    "protobuf-devel",
    "linux-headers",
    "gtest-devel",
]
depends = ["python", "android-udev-rules"]
pkgdesc = "Android platform tools (e.g. adb and fastboot)"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0 AND ISC AND GPL-2.0-only AND MIT"
url = "https://github.com/nmeum/android-tools"
source = f"{url}/releases/download/{pkgver}/android-tools-{pkgver}.tar.xz"
sha256 = "7a22ff9cea81ff4f38f560687858e8f8fb733624412597e3cc1ab0262f8da3a1"
tool_flags = {"CXXFLAGS": ["-D_LARGEFILE64_SOURCE"]}
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("vendor/boringssl/LICENSE", name="boringssl.LICENSE")
    self.install_license(
        "vendor/boringssl/third_party/fiat/LICENSE", name="fiat.LICENSE"
    )
