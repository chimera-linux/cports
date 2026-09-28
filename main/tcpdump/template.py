pkgname = "tcpdump"
pkgver = "4.99.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_SMB=ON"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "linux-headers", "pkgconf"]
makedepends = ["libpcap-devel", "openssl3-devel"]
checkdepends = ["perl"]
pkgdesc = "Command-line network traffic analysis tool"
license = "BSD-3-Clause"
url = "https://www.tcpdump.org"
source = f"https://www.tcpdump.org/release/tcpdump-{pkgver}.tar.gz"
sha256 = "5839921a0f67d7d8fa3dacd9cd41e44c89ccb867e8a6db216d62628c7fd14b09"


def post_install(self):
    self.install_license("LICENSE")
