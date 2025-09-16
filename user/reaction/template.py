pkgname = "reaction"
pkgver = "2.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera", "rust-std"]
pkgdesc = "Scans logs for repeated patterns and takes action"
license = "AGPL-3.0-or-later"
url = "https://reaction.ppom.me"
source = f"https://framagit.org/ppom/reaction/-/archive/v{pkgver}/reaction-v{pkgver}.tar.gz"
sha256 = "894cededfa22d8e1058830828ccedba21bd9ce2f744bbd539b224f9e71f95eea"
hardening = ["vis", "cfi"]

if self.profile().wordsize == 32:
    broken = "needs atomicu64"


def post_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(["helpers_c/ip46tables.c"], "ip46tables")
    cc.invoke(["helpers_c/nft46.c"], "nft46")


def install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("reaction")
        self.install_man("reaction*.1", glob=True)
    self.install_bin("ip46tables")
    self.install_bin("nft46")
    self.install_license("LICENSE")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "reaction")
    self.install_file("./config/example.jsonnet", "usr/share/reaction")
    self.install_file("./config/example.yml", "usr/share/reaction")
