pkgname = "beets"
pkgver = "2.14.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # beautifulsoup4
    "--ignore=test/plugins/test_fetchart.py",
    "--ignore=test/plugins/test_lyrics.py",
    # discogs_client
    "--ignore=test/plugins/test_discogs.py",
    # flakes
    "--ignore=test/test_importer.py",
    "--ignore=test/test_ui.py",
    # mpd
    "--ignore=test/plugins/test_mpdstats.py",
    # pylast
    "--ignore=test/plugins/test_lastgenre.py",
    # pytest fixture client not found
    "--ignore=test/plugins/test_aura.py",
    # requests_mock
    "--ignore=test/plugins/test_art.py",
    "--ignore=test/plugins/test_deezer.py",
    "--ignore=test/plugins/test_embedart.py",
    "--ignore=test/plugins/test_listenbrainz.py",
    "--ignore=test/plugins/test_mbcollection.py",
    "--ignore=test/plugins/test_missing.py",
    "--ignore=test/plugins/test_musicbrainz.py",
    "--ignore=test/plugins/test_parentwork.py",
    "--ignore=test/plugins/test_plexupdate.py",
    "--ignore=test/plugins/test_tidal.py",
    # requests_oauthlib
    "--ignore=test/plugins/test_beatport.py",
    # titlecase
    "--ignore=test/plugins/test_titlecase.py",
]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-confuse",
    "python-jellyfish",
    "python-lap",
    "python-mediafile",
    "python-munkres",
    "python-packaging",
    "python-platformdirs",
    "python-pyyaml",
    "python-requests",
    "python-requests-ratelimiter",
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
sha256 = "b25dc7bf8ed093d8b6e043e88013736902c1082c958b81a598af5db5275539a5"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/beet.1")
    self.install_man("man/beetsconfig.5")
