# update patches/version.patch on updates
pkgname = "beets"
pkgver = "2.5.1"
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
    # flakes
    "--ignore=test/test_importer.py",
    "--ignore=test/test_ui.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-confuse",
    "python-jellyfish",
    "python-lap",
    "python-mediafile",
    "python-munkres",
    "python-musicbrainzngs",
    "python-platformdirs",
    "python-pyyaml",
    "python-requests",
    "python-typing_extensions",
    "python-unidecode",
]
checkdepends = [
    "python-flask",
    "python-mock",
    "python-pytest-xdist",
    "python-pyxdg",
    "python-responses",
    *depends,
]
pkgdesc = "CLI media library management"
license = "MIT"
url = "https://beets.io"
source = f"$(PYPI_SITE)/b/beets/beets-{pkgver}.tar.gz"
sha256 = "7feefd70804fbcf26516089f472bac34c6a77e8e20ec539252fd1bafc91de9a2"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/beet.1")
    self.install_man("man/beetsconfig.5")
