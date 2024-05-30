pkgname = "reaction"
pkgver = "1.4.0"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X main.version={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Scans logs for repeated patterns and takes action"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://reaction.ppom.me"
source = f"https://framagit.org/ppom/reaction/-/archive/v{pkgver}/reaction-v{pkgver}.tar.gz"
sha256 = "fb4697384a1d9859fd6afb395294602a4b0af0b2effbba7aab6d1d88b53171e7"
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
