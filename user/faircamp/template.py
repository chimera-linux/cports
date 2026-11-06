pkgname = "faircamp"
pkgver = "2.0.1"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "faircamp", "--bin", "faircamp-cli"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["fontconfig-devel", "opus-devel", "zstd-devel"]
depends = ["ffmpeg", "rsync"]
pkgdesc = "Static site generator for audio producers"
license = "AGPL-3.0-or-later AND OFL-1.1"
url = "https://faircamp.org"
source = f"https://codeberg.org/simonrepp/faircamp/archive/{pkgver}.tar.gz"
sha256 = "c3518bb1a54609475ba7452f2e4b0fe82199818700083a0cd69d8997f59a4585"


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
