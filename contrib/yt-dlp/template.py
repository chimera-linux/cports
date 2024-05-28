pkgname = "yt-dlp"
pkgver = "2024.05.27"
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
sha256 = "718cc1e0b7a89a18d35fad0b5ad50fe37bf2aa4ff47bde374328ddca79670a3c"
# missing checkdepends
options = ["!check"]
