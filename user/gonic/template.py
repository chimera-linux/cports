pkgname = "gonic"
pkgver = "0.19.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/gonic"]
hostmakedepends = ["go", "pkgconf"]
makedepends = ["dinit-chimera", "sqlite-devel"]
depends = ["ffmpeg"]
checkdepends = [*depends]
go_build_tags = ["libsqlite3", "nowasm"]
pkgdesc = "Music streaming server / subsonic server API implementation"
license = "GPL-3.0-only"
url = "https://github.com/sentriz/gonic"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "929169a79ff498e08f80e4ed9d0949e87cbbf75769a7d1c6bd4cedf322bbad71"


def post_install(self):
    self.install_service(self.files_path / "gonic")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file("contrib/config", "etc/gonic/")
