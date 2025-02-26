pkgname = "soju"
pkgver = "0.8.2"
_commit = "5ee7ed56f7ed4ad0ccba13d944b5610fa46de352"
pkgrel = 0
build_style = "makefile"
make_build_args = ["GOFLAGS=-buildmode=pie -tags=libsqlite3"]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
makedepends = ["sqlite-devel"]
pkgdesc = "User-friendly IRC bouncer"
maintainer = "sewn <sewn@disroot.org>"
license = "AGPL-3.0-only"
url = "https://soju.im"
source = f"https://codeberg.org/emersion/soju/archive/{_commit}.tar.gz"
sha256 = "f80dc523da94900704072889965ccbb51ca15a5102c5b57524c2a45abae7122e"
file_modes = {
    "usr/bin/soju": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/soju": {"security.capability": "cap_net_bind_service+ep"},
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
    self.install_service(self.files_path / "soju")
    self.install_license("LICENSE")
