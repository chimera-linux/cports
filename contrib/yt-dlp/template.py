pkgname = "yt-dlp"
pkgver = "2023.06.22"
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
sha256 = "6eba89cbcac49b2dab21bbd9ad272c88fb1e97503c839b6fe72e99c02539940e"
# missing checkdepends
options = ["!check"]
