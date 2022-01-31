pkgname = "yt-dlp"
pkgver = "2022.01.21"
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
source = f"{url}/releases/download/{pkgver}/{pkgname}.tar.gz"
sha256 = "78455c03fb3f5a84bfc05afca5a2564af9852e8fe7f088877e20b8508217dd29"
# missing checkdepends
options = ["!check"]
