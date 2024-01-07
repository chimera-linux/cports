pkgname = "yt-dlp"
pkgver = "2023.12.30"
pkgrel = 1
build_style = "python_pep517"
make_check_args = ["-k", "not download"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-nose", "flake8"]
depends = ["python"]
pkgdesc = "CLI program to download videos from YouTube and other sites"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2878501990f3ab6aa8eabb7346c16d4b4cbc01984372a1f0b3a6be8d260c7aff"
# missing checkdepends
options = ["!check"]
