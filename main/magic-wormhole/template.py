pkgname = "magic-wormhole"
pkgver = "0.18.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-versioneer",
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
    "python-qrcode",
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
license = "MIT"
url = "https://magic-wormhole.readthedocs.io"
source = f"$(PYPI_SITE)/m/magic-wormhole/magic-wormhole-{pkgver}.tar.gz"
sha256 = "66fdee0861ec63ab494560aa1c68ebe3b21e955d0cabd84eadf93013e332852c"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        # needs some locale folder
        "--deselect=src/wormhole/test/test_cli.py",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("docs/wormhole.1")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"wormhole_complete.{shell}", shell, "wormhole")

    self.uninstall("usr/lib/python*/site-packages/wormhole/test", glob=True)
    self.uninstall("usr/wormhole_complete*", glob=True)
