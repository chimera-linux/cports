pkgname = "yt-dlp"
pkgver = "2023.03.04"
pkgrel = 0
build_style = "python_module"
make_check_args = ["-k", "not download"]
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest", "python-nose", "flake8"]
depends = ["python"]
pkgdesc = "CLI program to download videos from YouTube and other sites"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5e5abfe78b8f92f8b8307231d1e7ed0e462407f4cd861b48a0278559612de9aa"
# missing checkdepends
options = ["!check"]
