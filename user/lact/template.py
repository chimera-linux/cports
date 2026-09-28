pkgname = "lact"
pkgver = "0.10.1"
pkgrel = 0
_release_tag = "30dc182"
build_style = "cargo"
make_build_env = {"VERGEN_GIT_SHA": _release_tag}
make_check_args = [
    "--",
    # fails in cbuild container
    "--skip=tests::apply_settings",
    # fails on several archs due to vram diff?
    "--skip=tests::snapshot_everything",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "libadwaita-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
]
depends = [
    "clinfo",
    "hwdata-pci",
    "vulkan-tools",
]
pkgdesc = "GPU configuration and monitoring tool"
license = "MIT"
url = "https://github.com/ilya-zlobintsev/LACT"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cbbbd0336fb65ce539ea29d99fe2e38f7c82de08c07d26dfab355735a88d853c"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "lact"))

    pfx = "res/io.github.ilya_zlobintsev.LACT"

    self.install_file(f"{pfx}.desktop", "usr/share/applications")
    self.install_file(f"{pfx}.metainfo.xml", "usr/share/metainfo")
    self.install_file(f"{pfx}.png", "usr/share/icons/hicolor/512x512/apps")
    for f in ["-symbolic", ".Devel", ".Source", ""]:
        self.install_file(
            f"{pfx}{f}.svg", "usr/share/icons/hicolor/scalable/apps"
        )

    self.install_service(self.files_path / "lact")
    self.install_license("LICENSE")
