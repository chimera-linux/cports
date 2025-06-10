pkgname = "snort"
pkgver = "3.8.1.0"
pkgrel = 0
build_style = "cmake"
# "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
configure_args = [
    "-DDNET_INCLUDE_DIR=/usr/include/dnet",
    "-DENABLE_LARGE_PCAP=ON",
    "-DENABLE_SHELL=ON",
]
hostmakedepends = ["cmake", "flex", "ninja", "pkgconf"]
makedepends = [
    "daq-devel-static",
    "hwloc-devel",
    "libdnet-devel",
    "libpcap-devel",
    "libtirpc-devel",
    "luajit-devel",
    "numactl-devel",
    "openssl3-devel",
    "pcre2-devel",
    "util-linux-uuid-devel",
    "xz-devel",
]
depends = ["bash"]
pkgdesc = "Network intrusion prevention and detection system"
license = "GPL-2.0-only"
url = "https://www.snort.org"
source = f"https://github.com/snort3/snort3/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "adbd958bd0f9b2c78997bfda5a36cbbc843f07a71712db0b56f085e2cd124164"


@subpackage("snort-devel")
def _(self):
    return self.default_devel()
