pkgname = "beets"
pkgver = "2.2.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # pytest fixture client not found
    "--ignore=test/plugins/test_aura.py",
    # requests_oauthlib
    "--ignore=test/plugins/test_beatport.py",
    # discogs_client
    "--ignore=test/plugins/test_discogs.py",
    # pylast
    "--ignore=test/plugins/test_lastgenre.py",
    # mpd
    "--ignore=test/plugins/test_mpdstats.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-confuse",
    "python-jellyfish",
    "python-mediafile",
    "python-munkres",
    "python-musicbrainzngs",
    "python-platformdirs",
    "python-unidecode",
    "python-pyyaml",
    "python-requests",
]
checkdepends = [
    "python-flask",
    "python-pytest-xdist",
    "python-pyxdg",
    "python-responses",
    *depends,
]
pkgdesc = "CLI media library management"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "MIT"
url = "https://beets.io"
source = f"$(PYPI_SITE)/b/beets/beets-{pkgver}.tar.gz"
sha256 = "cc0a277f530844575e3374021f316da16bf78ed514963c1ab1597168a8d4c715"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/beet.1")
    self.install_man("man/beetsconfig.5")
