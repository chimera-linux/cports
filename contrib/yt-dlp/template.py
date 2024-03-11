pkgname = "yt-dlp"
pkgver = "2024.03.10"
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
sha256 = "079dbf54586e8120c7d76e0dd1b7a60e6c13f4d23f9681fc919577f2fe17d8cd"
# missing checkdepends
options = ["!check"]
