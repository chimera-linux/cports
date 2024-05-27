pkgname = "yt-dlp"
pkgver = "2024.05.26"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["-k", "not download"]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-nose", "flake8"]
depends = ["python", "python-certifi"]
pkgdesc = "CLI program to download videos from YouTube and other sites"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8daf63bd8c63970d8f49d67a539da2e6f3628c3006e8daf53276b96790384b40"
# missing checkdepends
options = ["!check"]
