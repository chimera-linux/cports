pkgname = "zrepl"
pkgver = "0.9.6"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
depends = ["zfs"]
pkgdesc = "ZFS backup and replication tool - dsh2dsh's enhanced fork"
maintainer = "Robert David <robert.david@posteo.net>"
license = "MIT"
url = "https://github.com/dsh2dsh/zrepl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0c2e805cb9aaabb30dcf66ea8a26d51370420753b0e0960114498b9a7789d609"
# check needs to run zfs command
options = ["!check"]


def install(self):
    self.install_bin("build/zrepl")
    self.install_files(
        "internal/config/samples", "usr/share/examples", name="zrepl"
    )
    self.install_file(
        "dist/freebsd/etc/zrepl/zrepl.yml", "usr/share/examples/zrepl"
    )
    self.install_service(self.files_path / "zrepl")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_license("LICENSE")
