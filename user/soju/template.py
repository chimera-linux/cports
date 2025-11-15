pkgname = "soju"
pkgver = "0.9.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    " -X codeberg.org/emersion/soju/config.DefaultPath=/etc/soju/config"
    " -X codeberg.org/emersion/soju/config.DefaultUnixAdminPath=/run/soju/admin",
    "./contrib/...",
    "./cmd/...",
]
hostmakedepends = ["go", "scdoc", "libcap-progs"]
makedepends = ["dinit-chimera", "sqlite-devel"]
go_build_tags = ["libsqlite3"]
pkgdesc = "IRC bouncer"
license = "AGPL-3.0-only"
url = "https://soju.im"
source = f"https://codeberg.org/emersion/soju/archive/v{pkgver}.tar.gz"
sha256 = "3ca05f741342f60a385e2c3c784824e81c122b05a909efe0fa62b94c414f92f1"
file_modes = {
    "usr/bin/soju": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/soju": {"security.capability": "cap_net_bind_service+ep"},
}
# no tests
options = ["!check"]


def post_build(self):
    self.do("make", "doc/soju.1", "doc/sojuctl.1")


def install(self):
    for util in ["migrate-db", "migrate-logs", "znc-import"]:
        self.install_bin(f"{self.make_dir}/{util}", name=f"soju-{util}")
    self.install_bin(f"{self.make_dir}/soju*", glob=True)
    self.install_file("contrib/casemap-logs.sh", "usr/lib/soju", mode=0o755)

    self.install_man("doc/soju.1")
    self.install_man("doc/sojuctl.1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "soju")
    self.install_license("LICENSE")


@subpackage("soju-utils")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/soju-*",
        "usr/lib/soju/casemap-logs.sh",
    ]
