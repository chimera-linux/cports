pkgname = "zed"
pkgver = "0.163.2"
pkgrel = 0
# wasmtime
archs = ["aarch64", "x86_64"]
build_style = "cargo"
make_build_args = ["--package", "zed", "--package", "cli"]
make_build_env = {
    "RELEASE_VERSION": pkgver,
    "ZED_UPDATE_EXPLANATION": "Managed by system package manager",
}
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protoc",
]
makedepends = [
    "alsa-lib-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libcurl-devel",
    "libgit2-devel",
    "libxkbcommon-devel",
    "rust-std",
    "sqlite-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
# otherwise downloads a non-working one
depends = ["nodejs"]
pkgdesc = "Graphical text editor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later AND AGPL-3.0-or-later AND Apache-2.0"
url = "https://zed.dev"
source = (
    f"https://github.com/zed-industries/zed/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "d0c6cc6727ba229ef1a912cd238554651242a3d1569ab27c534c66f4f8e098f9"
# workaround code that fails with default gc-sections with lld
# https://github.com/zed-industries/zed/issues/15902
tool_flags = {"RUSTFLAGS": ["-Clink-arg=-Wl,-z,nostart-stop-gc"]}
# no
options = ["!check", "!cross"]


def install(self):
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli", name="zeditor"
    )
    self.install_file(
        f"target/{self.profile().triplet}/release/zed",
        "usr/lib/zed",
        name="zed-editor",
    )
    self.install_file(
        "crates/zed/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="zed.png",
    )
    self.install_file(
        "crates/zed/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="zed.png",
    )
    self.install_file(
        "crates/zed/resources/zed.desktop.in",
        "usr/share/applications",
        name="zed.desktop",
    )
    self.install_license("LICENSE-AGPL")
