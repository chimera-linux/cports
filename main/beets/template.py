pkgname = "beets"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # python-reflink
    "--deselect=test/test_files.py::MoveTest::test_reflink_arrives",
    "--deselect=test/test_files.py::MoveTest::test_reflink_does_not_depart",
    "--config-file=/dev/null",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-confuse",
    "python-jellyfish",
    "python-mediafile",
    "python-munkres",
    "python-musicbrainzngs",
    "python-unidecode",
    "python-pyyaml",
    "python-requests",
]
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "CLI media library management"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "MIT"
url = "https://beets.io"
source = f"$(PYPI_SITE)/b/beets/beets-{pkgver}.tar.gz"
sha256 = "3b1172b5bc3729e33a6ea4689f7d0236682bf828c67196b6a260f0389cb1f8cf"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/beet.1")
    self.install_man("man/beetsconfig.5")
