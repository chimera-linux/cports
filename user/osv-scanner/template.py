pkgname = "osv-scanner"
pkgver = "2.3.3"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.version={pkgver}",
    f"./cmd/{pkgname}",
]
hostmakedepends = ["go"]
pkgdesc = "Vulnerability scanner"
license = "Apache-2.0"
url = "https://github.com/google/osv-scanner"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "05a87a6b658eafa473b2e08316491551d9402501f67a731043c677c435a12a32"
# osv-scanner tests requires network connection
options = ["!check"]
