pkgname = "igmpproxy"
pkgver = "0.4"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake"]
makedepends = ["dinit-chimera", "linux-headers"]
pkgdesc = "Multicast forwarding IGMP proxy"
license = "GPL-2.0-or-later"
url = "https://github.com/pali/igmpproxy"
source = f"{url}/releases/download/{pkgver}/igmpproxy-{pkgver}.tar.gz"
sha256 = "afa4b75a823b82f71ce99f33eae4e8136b906ae8a5ede5caaad93bac38cdae24"
# Not available
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "igmpproxy")
