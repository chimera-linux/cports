pkgname = "tcpdump"
pkgver = "4.99.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_SMB=ON"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "linux-headers", "pkgconf"]
makedepends = ["libpcap-devel", "openssl3-devel"]
checkdepends = ["perl"]
pkgdesc = "Command-line network traffic analysis tool"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://www.tcpdump.org"
source = f"https://www.tcpdump.org/release/tcpdump-{pkgver}.tar.gz"
sha256 = "8c75856e00addeeadf70dad67c9ff3dd368536b2b8563abf6854d7c764cd3adb"


def post_install(self):
    self.install_license("LICENSE")
