pkgname = "yt-dlp"
pkgver = "2025.12.08"
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
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = (
    f"{url}/releases/download/{pkgver}/yt-dlp.tar.gz>yt-dlp-{pkgver}.tar.gz"
)
sha256 = "9814ae7dd4118a80a6104399d4984e355d2a71f78e6bbc48137a5b299eddcbaf"


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
