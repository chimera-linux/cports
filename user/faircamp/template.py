pkgname = "faircamp"
pkgver = "2.0.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "faircamp", "--bin", "faircamp-cli"]
hostmakedepends = ["cargo-auditable", "pkgconf", "cmake"]
makedepends = ["fontconfig-devel", "opus-devel", "zstd-devel"]
depends = ["ffmpeg", "rsync"]
pkgdesc = "Static site generator for audio producers"
license = "AGPL-3.0-or-later AND OFL-1.1"
url = "https://faircamp.org"
source = f"https://codeberg.org/simonrepp/faircamp/archive/{pkgver}.tar.gz"
sha256 = "97046d78d8c09837067ae9290fe7aecf5dbb3eb107c1346583534fcb715349f0"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "faircamp"))
    self.install_bin(cargo.target_path(self, "faircamp-cli"))

    self.install_file(
        self.files_path / "org.faircamp.Faircamp.desktop",
        "usr/share/applications",
    )
    self.install_file(
        "assets/favicon.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="faircamp.svg",
    )

    self.install_license("LICENSES/AGPL-3.0-or-later.txt")
    self.install_license("LICENSES/OFL-1.1.txt")
