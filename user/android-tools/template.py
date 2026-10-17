pkgname = "android-tools"
pkgver = "37.0.0_p1"
_realver = pkgver.replace("_", "")
pkgrel = 0
# only supports specific little-endian archs, particularly in boringssl
archs = ["x86_64", "aarch64", "loongarch64", "ppc64le", "riscv64"]
build_style = "cmake"
configure_args = ["-DANDROID_TOOLS_ADB_ENABLE_MDNS=ON"]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "corrosion",
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
    "rust-std",
    "zstd-devel",
]
depends = ["android-udev-rules", "python"]
pkgdesc = "Android platform tools, such as adb and fastboot"
license = "Apache-2.0 AND ISC AND GPL-2.0-only AND MIT"
url = "https://github.com/nmeum/android-tools"
source = f"{url}/releases/download/{_realver}/android-tools-{_realver}.tar.xz"
sha256 = "2c6de1abe16b211c7d9f59276217e14fd9e0e18b20e331d3c84358f5dffd576e"
tool_flags = {"CXXFLAGS": ["-D_LARGEFILE64_SOURCE"]}
hardening = ["vis", "cfi"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="vendor/adb/client/adbmdns").vendor()


def post_install(self):
    self.install_license("vendor/boringssl/LICENSE", name="boringssl.LICENSE")
    self.install_license(
        "vendor/boringssl/third_party/fiat/LICENSE", name="fiat.LICENSE"
    )
