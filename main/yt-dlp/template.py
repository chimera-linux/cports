pkgname = "yt-dlp"
pkgver = "2026.07.04"
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
sha256 = "31c32457d1a573a341bb0929386c624fe47339a5338829e6e9c9454bdfa7397a"


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
    # don't pull in on platforms not supported by node, as that will prevent
    # building yt-dlp on platforms that can't build yt-dlp-ejs
    if self.rparent.profile().arch in [
        "aarch64",
        "loongarch64",
        "ppc64le",
        "riscv64",
        "x86_64",
    ]:
        self.depends += ["yt-dlp-ejs"]
    self.subdesc = "recommended dependencies"
    self.install_if = [self.parent]
    self.options = ["empty"]
    return []
