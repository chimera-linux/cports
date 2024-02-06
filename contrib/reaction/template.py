pkgname = "reaction"
pkgver = "1.3.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Scans logs for repeated patterns and takes action"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://reaction.ppom.me"
source = f"https://framagit.org/ppom/reaction/-/archive/v{pkgver}/reaction-v{pkgver}.tar.gz"
sha256 = "a0dc8459cf6ad377287ca93a4d35077938f3eaa5ef53017f3a92ef785c535953"
# no tests defined
options = ["!check"]


def post_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)
    cc.invoke(["helpers_c/ip46tables.c"], "ip46tables")
    cc.invoke(["helpers_c/nft46.c"], "nft46")


def post_install(self):
    self.install_bin("ip46tables")
    self.install_bin("nft46")
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="reaction.conf",
    )
    self.install_service(self.files_path / "reaction")
    self.install_file("./app/example.yml", "etc/reaction", name="reaction.yml")
