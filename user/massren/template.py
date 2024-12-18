pkgname = "massren"
pkgver = "1.5.7"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["sqlite-devel"]
go_build_tags = ["libsqlite3"]
go_check_tags = ["libsqlite3"]
pkgdesc = "Rename multiple files using any text editor"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/laurent22/massren"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7e7dd149bd3364235247268cc684b5a35badd9bee22f39960e075c792d037a8c"
options = ["!distlicense"]


def post_extract(self):
    self.rm("vendor", recursive=True)
