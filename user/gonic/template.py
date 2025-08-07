pkgname = "gonic"
pkgver = "0.16.4"
pkgrel = 11
build_style = "go"
make_build_args = ["./cmd/gonic"]
hostmakedepends = ["go", "pkgconf"]
makedepends = ["sqlite-devel", "taglib-devel"]
depends = ["ffmpeg"]
checkdepends = [*depends]
go_build_tags = ["libsqlite3"]
pkgdesc = "Music streaming server / subsonic server API implementation"
license = "GPL-3.0-only"
url = "https://github.com/sentriz/gonic"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ba690a861a075bdf3f1f7e8131e45a5ca430ec90902a97faf955ec9f36799461"
# taglib gomod can't cross
options = ["!cross"]


def post_install(self):
    self.install_service(self.files_path / "gonic")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file("contrib/config", "etc/gonic/")
