pkgname = "tlstunnel"
pkgver = "0.3.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["GOFLAGS=-buildmode=pie"]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
pkgdesc = "TLS reverse proxy"
maintainer = "sewn <sewn@disroot.org>"
license = "MIT"
url = "https://git.sr.ht/~emersion/tlstunnel"
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


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "tlstunnel")
    self.install_license("LICENSE")
