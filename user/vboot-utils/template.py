pkgname = "vboot-utils"
pkgver = "110.15278"
_release = "release-R110-15278.B"
pkgrel = 0
build_style = "makefile"
make_build_args = ["TPM2_MODE=1", "V=1"]
make_use_env = True
hostmakedepends = ["bash", "pkgconf"]
makedepends = [
    "chimerautils-devel",
    "flashrom-devel",
    "linux-headers",
    "openssl3-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "ChromeOS verified boot utilities"
license = "custom:chromiumos"
url = "https://chromium.googlesource.com/chromiumos/platform/vboot_reference"
# Chromiumsource tarball download produced a different sha256sum each time for some reason
source = (
    f"https://github.com/coreboot/vboot/archive/refs/heads/{_release}.tar.gz"
)
sha256 = "bbfca2b06d5f3b785f92ac2eb95ee77612ba7ec5c1cfa0e246d24534d3cef045"
# Tests fail
options = ["!check"]


def install(self):
    self.install_bin("build/futility/futility")
    self.install_bin("build/cgpt/cgpt")
    self.install_bin("build/utility/crossystem")
    self.install_bin("build/utility/tpmc")
    self.install_files("tests/devkeys", "usr/share/vboot")
    self.install_license("LICENSE")
