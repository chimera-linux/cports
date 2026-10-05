pkgname = "trurl"
pkgver = "0.16.1"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
makedepends = ["curl-devel"]
checkdepends = ["python"]
pkgdesc = "Command line tool for URL parsing and manipulation"
license = "curl"
url = "https://curl.se/trurl"
source = f"{url}/dl/trurl-{pkgver}.tar.gz"
sha256 = "aac947d4fb421a58abc19a3771e87942cd4721b8f855c433478c94c11a8203ba"
hardening = ["vis", "cfi"]
# 14 test failures; all due to case mismatches
# upstream: https://github.com/curl/trurl/issues/440
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
