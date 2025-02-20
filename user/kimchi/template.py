pkgname = "kimchi"
pkgver = "0.1.0"
pkgrel = 0
build_style = "go"
make_build_args = ["-ldflags=-X main.configPath=/etc/kimchi/config"]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
pkgdesc = "Bare-bones HTTP server"
license = "MIT"
url = "https://codeberg.org/emersion/kimchi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "224ff49a9aee6209394d5230aec0477f1a6a66e5af70dfc45fb29365d64bcd07"
file_modes = {
    "usr/bin/kimchi": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/kimchi": {"security.capability": "cap_net_bind_service+ep"},
}
# no tests
options = ["!check"]


def pre_build(self):
    self.do("make", "kimchi.1")


def post_install(self):
    self.install_man("kimchi.1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "kimchi")
    self.install_license("LICENSE")
