pkgname = "magic-wormhole"
pkgver = "0.14.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-attrs",
    "python-autobahn",
    "python-automat",
    "python-click",
    "python-cryptography",
    "python-humanize",
    "python-iterable-io",
    "python-pynacl",
    "python-spake2",
    "python-tqdm",
    "python-twisted",
    "python-txtorcon",
    "python-zipstream-ng",
]
checkdepends = [
    "magic-wormhole-mailbox-server",
    "magic-wormhole-transit-relay",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Utility to transfer data between computers"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://magic-wormhole.readthedocs.io"
source = f"$(PYPI_SITE)/m/magic-wormhole/magic-wormhole-{pkgver}.tar.gz"
sha256 = "006d239f88bff7c37bc2eff60a004e263faf9258f7279192d06ba0c9ced6b080"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        # needs some locale folder
        "--deselect=src/wormhole/test/test_cli.py",
        # needs net
        "--deselect=src/wormhole/test/dilate/test_record.py",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("docs/wormhole.1")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wormhole_complete.{shell}", shell, "wormhole")

    self.uninstall("usr/lib/python*/site-packages/wormhole/test", glob=True)
    self.uninstall("usr/wormhole_complete*", glob=True)
