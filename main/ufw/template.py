pkgname = "ufw"
pkgver = "0.36.1"
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
sha256 = "1c57e78fbf2970f0cc9c56ea87a231e6d83d825e55b9e31e2c88b91b0ea03c8c"
# needs itself installed
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "ufw")
