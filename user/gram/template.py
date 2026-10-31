pkgname = "gram"
pkgver = "3.4.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "gram", "-p", "cli", "-p", "remote_server"]
make_build_env = {
    "GRAM_NO_BUNDLED_UNINSTALL": "Use apk to uninstall",
}
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protobuf-protoc",
]
makedepends = [
    "libssh2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "openssl3-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = [
    "clang",
    "nodejs",
    "rust-wasm",
    "wasi-clang",
    "wasm-component-ld",
]
pkgdesc = "Code editor forked from Zed"
license = "GPL-3.0-or-later"
url = "https://gram-editor.com"
source = f"https://codeberg.org/GramEditor/gram/archive/{pkgver}.tar.gz"
sha256 = "c15d11a4af69ae5c9f33906b85df649b6436cd2eff64b3a0039417c440b33472"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "cli"), name="gram")
    self.install_bin(
        cargo.target_path(self, "remote_server"), name="gram-remote-server"
    )
    self.install_file(
        cargo.target_path(self, "gram"),
        "usr/lib/gram",
        mode=0o755,
        name="gram-editor",
    )

    res = "crates/gram/resources"
    self.install_file(
        f"{res}/gram.desktop.in",
        "usr/share/applications",
        name="app.liten.Gram.desktop",
        template={
            "APP_NAME": "Gram",
            "APP_CLI": "/usr/bin/gram",
            "APP_ICON": "app.liten.Gram",
            "APP_ARGS": "%U",
            "DO_STARTUP_NOTIFY": "false",
        },
        pattern=r"\$(\w+)",
    )
    self.install_file(
        f"{res}/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        f"{res}/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        f"{res}/app.liten.Gram.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
