pkgname = "ufw"
pkgver = "0.36.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "gmake", "iptables"]
depends = [
    "iptables",
    "python",
    "virtual:cmd:modprobe!kmod",
    "virtual:cmd:sysctl!procps",
]
pkgdesc = "Uncomplicated Firewall"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://launchpad.net/ufw"
source = f"{url}/{pkgver[:-2]}/{pkgver}/+download/{pkgname}-{pkgver}.tar.gz"
sha256 = "2a57a99eecef6b44db3537ed2520b30bae3759f8465456e22e404cd643838bf5"
# needs itself installed
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "ufw")
