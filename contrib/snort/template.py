pkgname = "snort"
pkgver = "3.3.5.0"
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
    "libnuma-devel",
    "libpcap-devel",
    "libtirpc-devel",
    "libuuid-devel",
    "luajit-devel",
    "openssl-devel",
    "pcre-devel",
]
depends = ["bash"]
pkgdesc = "Network intrusion prevention and detection system"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "GPL-2.0-only"
url = "https://www.snort.org"
source = f"https://github.com/snort3/snort3/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b87f5db610d869c11769d795c6cce7646baa930d6ba2509460add28cb4a028bf"


@subpackage("snort-devel")
def _(self):
    return self.default_devel()
