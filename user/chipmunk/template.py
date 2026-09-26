pkgname = "chipmunk"
pkgver = "4.3.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "openssl3-devel", "zstd-devel"]
pkgdesc = "Log analysis tool"
license = "Apache-2.0"
url = "https://github.com/esrlabs/chipmunk"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9b8c3c9d5bdcd4ab6040fe0820907608e4435886cff20ef674274f4cb5685fe9"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "chipmunk"))
    self.install_file(
        "crates/app/data/linux/chipmunk.desktop",
        "usr/share/applications",
    )
    self.install_file(
        "crates/app/data/linux/chipmunk.png",
        "usr/share/icons/hicolor/512x512/apps",
    )
    self.install_license("LICENSE.txt")
