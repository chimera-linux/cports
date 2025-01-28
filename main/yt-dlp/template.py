pkgname = "yt-dlp"
pkgver = "2025.01.26"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--deselect=test/test_socks.py",
    "-k",
    "not download and not test_verify_cert and not test_mtls",
]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-wheel",
]
depends = ["python-certifi"]
checkdepends = [
    "python-brotli",
    "python-pytest-xdist",
    "python-requests",
    "python-websockets",
    *depends,
]
pkgdesc = "CLI program to download videos from YouTube and other sites"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5face0597286f9bee3bfe3196a3fb30badeeff2104c4f4ca2bcaa69ba85be255"


@subpackage("yt-dlp-recommends")
def _(self):
    self.depends = [
        "ffmpeg",
        "mutagen",
        "python-brotli",
        "python-pycryptodomex",
        "python-secretstorage",
        "python-websockets",
    ]
    self.subdesc = "recommended dependencies"
    self.install_if = [self.parent]
    self.options = ["empty"]
    return []
