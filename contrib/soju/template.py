pkgname = "soju"
pkgver = "0.7.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags="
    " -X git.sr.ht/~emersion/soju/config.DefaultPath=/etc/config/soju"
    " -X git.sr.ht/~emersion/soju/config.DefaultUnixAdminPath=/run/soju/admin",
    "./contrib/...",
    "./cmd/...",
]
hostmakedepends = ["go", "scdoc"]
makedepends = ["sqlite-devel"]
depends = ["ca-certificates", "libcap-progs"]
go_build_tags = ["libsqlite3"]
go_check_tags = list(go_build_tags)
pkgdesc = "IRC bouncer"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://soju.im"
source = f"https://git.sr.ht/~emersion/soju/archive/v{pkgver}.tar.gz"
sha256 = "089b900ccd7fa009b7ae50b9c2b9e77099b50b2499422649c3b27aff7d62d109"


def post_build(self):
    self.do("make", "doc/soju.1", "doc/sojuctl.1")


def do_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "soju")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="soju.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="soju.conf",
    )
    for util in [
        "migrate-db",
        "migrate-logs",
        "znc-import",
    ]:
        self.install_bin(f"{self.make_dir}/{util}", name=f"soju-{util}")
    self.install_bin(f"{self.make_dir}/soju*", glob=True)
    self.install_file("contrib/casemap-logs.sh", "usr/libexec", mode=0o755)
    self.install_man("doc/soju.1")
    self.install_man("doc/sojuctl.1")
    self.install_file("config.in", "etc/soju", name="config")


@subpackage("soju-utils")
def _utils(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/soju-*",
        "usr/libexec/casemap-logs.sh",
    ]
