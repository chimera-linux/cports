pkgname = "zrepl"
pkgver = "0.9.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["zfs"]
pkgdesc = "ZFS backup and replication tool - dsh2dsh's enhanced fork"
maintainer = "Robert David <robert.david@posteo.net>"
license = "MIT"
url = "https://github.com/dsh2dsh/zrepl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1262c854c32e66cf67dd1d8c2ca6e546b6d42100c9bca9857ba37b6a16a5b1d1"
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
