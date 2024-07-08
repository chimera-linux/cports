pkgname = "yt-dlp"
pkgver = "2024.07.08"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["-k", "not download"]
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-wheel",
]
depends = ["python-certifi"]
checkdepends = [
    "python-brotli",
    "python-pytest-xdist",
    "python-requests",
    "python-websockets",
] + depends
pkgdesc = "CLI program to download videos from YouTube and other sites"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/yt-dlp/yt-dlp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9a6ecee38746d3e9a74cdfb6938b4711646854c695ef7cf01ad11572d36d4ea3"
