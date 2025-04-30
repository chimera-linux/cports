pkgname = "salt-lts"
pkgver = "3006.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-certifi",
    "python-croniter",
    "python-cryptography",
    "python-distro",
    "python-jinja2",
    "python-jmespath",
    "python-looseversion",
    "python-markupsafe",
    "python-msgpack",
    "python-packaging",
    "python-psutil",
    "python-pycryptodomex",
    "python-pyyaml",
    "python-pyzmq",
    "python-requests",
    "python-tornado",
    "python-urllib3",
]
pkgdesc = "Distributed remote execution and configuration management system"
license = "Apache-2.0"
url = "http://github.com/saltstack/salt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9b2ef98a684b460408b3e8e02f342e0a55f1a48c3eeeae0aaa162d723f39e3d8"
# depends on pytestsalt
options = ["!check"]


def install(self):
    self.do(
        "python",
        "setup.py",
        "install",
        "--prefix=/usr",
        f"--root={self.chroot_destdir}",
    )


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_dir("etc/salt")
    for f in ["cloud", "master", "minion", "proxy"]:
        self.install_file(f"conf/{f}", "etc/salt")
    self.install_service(self.files_path / "salt-api")
    self.install_service(self.files_path / "salt-master")
    self.install_service(self.files_path / "salt-minion")
    self.install_service(self.files_path / "salt-syndic")
