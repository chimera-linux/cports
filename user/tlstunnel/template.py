pkgname = "tlstunnel"
pkgver = "0.4.0"
pkgrel = 3
build_style = "go"
make_build_args = [
    "-ldflags= "
    + "-X main.configPath=/etc/tlstunnel/config "
    + "-X main.certDataPath=/var/lib/tlstunnel",
    "./cmd/tlstunnel",
]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
makedepends = ["dinit-chimera"]
pkgdesc = "TLS reverse proxy"
license = "MIT"
url = "https://codeberg.org/emersion/tlstunnel"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "787d39adf16f1f57dde002286c7d32fe75da50db3e833a92f005c4effff5cd3f"
file_modes = {
    "usr/bin/tlstunnel": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/tlstunnel": {"security.capability": "cap_net_bind_service+ep"},
}
# no tests
options = ["!check"]


def pre_build(self):
    self.do("make", "tlstunnel.1")


def post_install(self):
    self.install_man("tlstunnel.1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "tlstunnel")
    self.install_license("LICENSE")
