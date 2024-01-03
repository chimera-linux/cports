pkgname = "ufw"
pkgver = "0.36.2"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "gmake",
    "iptables",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
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
    # /usr/lib already exists so need to move one at a time for merge..
    with self.pushd(self.destdir / "usr/lib/python*/site-packages", glob=True):
        self.mv("usr/share", self.destdir / "usr")
        self.mv("usr/lib/ufw", self.destdir / "usr/lib")
        self.mv("usr/bin", self.destdir / "usr")
        self.mv("etc", self.destdir)

    self.install_service(self.files_path / "ufw")
