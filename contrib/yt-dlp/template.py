pkgname = "yt-dlp"
pkgver = "2024.04.09"
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
sha256 = "fa2a21946b886f914ccc5ee18a9dc41b628745a51e04d136c6baec06ed4bded6"
# missing checkdepends
options = ["!check"]
