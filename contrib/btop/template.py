pkgname = "btop"
pkgver = "1.2.13"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Terminal resource monitor"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "668dc4782432564c35ad0d32748f972248cc5c5448c9009faeb3445282920e02"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]
