pkgname = "tcpdump"
pkgver = "4.99.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_SMB=ON"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "linux-headers"]
makedepends = ["libpcap-devel", "openssl-devel"]
checkdepends = ["perl"]
pkgdesc = "Command-line network traffic analysis tool"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "BSD-3-Clause"
url = "https://www.tcpdump.org"
source = f"https://www.tcpdump.org/release/{pkgname}-{pkgver}.tar.gz"
sha256 = "0232231bb2f29d6bf2426e70a08a7e0c63a0d59a9b44863b7f5e2357a6e49fea"


def post_install(self):
    self.install_license("LICENSE")
