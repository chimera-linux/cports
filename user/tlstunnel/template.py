pkgname = "tlstunnel"
pkgver = "0.3.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags= "
    + "-X main.configPath=/etc/tlstunnel/config "
    + "-X main.certDataPath=/var/lib/tlstunnel",
    "./cmd/tlstunnel",
]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
pkgdesc = "TLS reverse proxy"
license = "MIT"
url = "https://codeberg.org/emersion/tlstunnel"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fca4244dc2311e8b29704b68ab3a469c04cbea8bff5d7b80c3d5251a1477afdf"
file_modes = {
    "usr/bin/tlstunnel": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/tlstunnel": {"security.capability": "cap_net_bind_service+ep"},
}
# no tests
options = ["!check"]


def post_install(self):
    with open(self.cwd / "tlstunnel.1.scd", "rb") as i:
        with open(self.cwd / "tlstunnel.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)
            self.install_man(self.cwd / "tlstunnel.1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "tlstunnel")
    self.install_license("LICENSE")
