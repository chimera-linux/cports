pkgname = "zrepl"
pkgver = "0.9.8"
pkgrel = 4
build_style = "go"
hostmakedepends = ["go"]
depends = ["zfs"]
pkgdesc = "ZFS backup and replication tool - dsh2dsh's enhanced fork"
license = "MIT"
url = "https://github.com/dsh2dsh/zrepl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "069646e929c5440191d3240310a9fdb95b1258ac5ab2c15ab1eaee2022cb34fa"
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
