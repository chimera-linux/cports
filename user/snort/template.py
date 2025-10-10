pkgname = "snort"
pkgver = "3.9.6.0"
pkgrel = 0
build_style = "cmake"
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
license = "GPL-2.0-or-later"
url = "https://www.snort.org"
source = f"https://github.com/snort3/snort3/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2335678bc5ff4f876dcdb6985407a5312b0f3bb470da29e2926f57f942ce3b94"


@subpackage("snort-devel")
def _(self):
    return self.default_devel()
