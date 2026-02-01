pkgname = "yt-dlp"
pkgver = "2026.06.09"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "--deselect=test/test_socks.py",
    "--deselect=test/test_pot/test_pot_director.py",
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
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = (
    f"{url}/releases/download/{pkgver}/yt-dlp.tar.gz>yt-dlp-{pkgver}.tar.gz"
)
sha256 = "7603f876b78d08b5fdd5bcd1d368590fde22c3c18e4ea00766d51120d21cc679"


@subpackage("yt-dlp-recommends")
def _(self):
    self.depends = [
        "ffmpeg",
        "mutagen",
        "python-brotli",
        "python-pycryptodomex",
        "python-secretstorage",
        "python-websockets",
        "yt-dlp-ejs",
    ]
    self.subdesc = "recommended dependencies"
    self.install_if = [self.parent]
    self.options = ["empty"]
    return []
