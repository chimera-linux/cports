pkgname = "crosec-utils"
pkgver = "100.14526"
# Use an older release before ectool relied on libec and libchrome
_release = "release-R100-14526.B"
_gsc_release = "release-R116-15509.B"
pkgrel = 0
build_style = "makefile"
make_build_target = "utils"
make_build_args = ["BOARD=host", "V=1"]
make_use_env = True
hostmakedepends = ["bash", "pkgconf"]
makedepends = [
    "libftdi1-devel",
    "libusb-devel",
    "linux-headers",
    "openssl3-devel",
]
pkgdesc = "Chrome embedded controller utilities"
license = "custom:chromiumos"
url = "https://chromium.googlesource.com/chromiumos/platform/ec"
# Chromiumsource tarball download produced a different sha256sum each time for some reason
# gsctool is also part of the ec repo, but only included in gsc_utils branches
source = [
    f"https://github.com/coreboot/chrome-ec/archive/refs/heads/{_release}-main.tar.gz",
    f"https://github.com/coreboot/chrome-ec/archive/refs/heads/{_gsc_release}-gsc_utils.tar.gz",
]
source_paths = [".", "gsc_utils"]
sha256 = [
    "9e7b1a24a38bb7b9a0a2f00ef68aa6dfd12d043dc5360d187d4a83340ff7d41f",
    "0da06f71a2659e43f6442d7dcc1a0f39c83d423d68589a015f10162386bff269",
]
# No tests
options = ["!check"]


def post_build(self):
    self.make.invoke(["-C", "gsc_utils/extra/usb_updater"])


def install(self):
    utils = [
        "cbi-util",
        "ec_parse_panicinfo",
        "ec_sb_firmware_update",
        "ectool",
        "iteflash",
        "lbcc",
        "lbplay",
        "stm32mon",
        "uartupdatetool",
    ]
    for util in utils:
        self.install_bin(f"build/host/util/{util}")
    self.install_bin("gsc_utils/extra/usb_updater/gsctool")
    self.install_license("LICENSE")
