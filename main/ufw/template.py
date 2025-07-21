pkgname = "ufw"
pkgver = "0.36.2"
pkgrel = 3
build_style = "python_pep517"
hostmakedepends = [
    "iptables",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "cmd:modprobe!kmod",
    "cmd:sysctl!procps",
    "iptables",
    "python",
]
pkgdesc = "Uncomplicated Firewall"
license = "GPL-3.0-only"
url = "https://launchpad.net/ufw"
source = f"{url}/{pkgver[:-2]}/{pkgver}/+download/ufw-{pkgver}.tar.gz"
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
