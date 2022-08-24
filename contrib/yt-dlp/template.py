pkgname = "yt-dlp"
pkgver = "2022.08.19"
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
sha256 = "8fbb5193d03f3a2c6098b9bdd08a8a856f5d75a071785366fe84c4efe18bf391"
# missing checkdepends
options = ["!check"]
