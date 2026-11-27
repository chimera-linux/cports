pkgname = "salt-lts"
pkgver = "3008.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-looseversion",
    "python-packaging",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["dinit-chimera"]
depends = [
    "python-certifi",
    "python-croniter",
    "python-cryptography",
    "python-distro",
    "python-idna",
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
    "python-xxhash",
]
pkgdesc = "Distributed remote execution and configuration management system"
license = "Apache-2.0"
url = "https://github.com/saltstack/salt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ceaf6730f1e795dda9d29466652a27a7663712c1a8090a9697eeb4b1adb8a21"
# depends on pytestsalt
options = ["!check"]


def pre_build(self):
    # no git metadata in the tarball, version would end up as 3008.0
    (self.cwd / "salt/_version.txt").write_text(f"{self.pkgver}\n")


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
    for f in ["cloud", "master", "minion", "proxy"]:
        self.install_file(f"conf/{f}", "usr/share/etc/salt")
    self.install_service(self.files_path / "salt-api")
    self.install_service(self.files_path / "salt-master")
    self.install_service(self.files_path / "salt-minion")
    self.install_service(self.files_path / "salt-syndic")
