pkgname = "reaction"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Scans logs for repeated patterns and takes action"
license = "AGPL-3.0-or-later"
url = "https://reaction.ppom.me"
source = f"https://framagit.org/ppom/reaction/-/archive/v{pkgver}/reaction-v{pkgver}.tar.gz"
sha256 = "3b6cf5a35214075ac792a93521044877db70f7090752326661ba484cd9ce296c"
hardening = ["vis", "cfi"]


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
