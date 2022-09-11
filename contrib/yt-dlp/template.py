pkgname = "yt-dlp"
pkgver = "2022.09.01"
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
sha256 = "5a479b31a838ecf62a69b7880d069013528d2944a5e4088b84ae4105bc07d6c1"
# missing checkdepends
options = ["!check"]
