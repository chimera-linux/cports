pkgname = "gram"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cargo"
make_env = {
    "RELEASE_VERSION": f"{pkgver}-chimera-linux-r{pkgrel}",
    "GRAM_UPDATE_EXPLANATION": "Update Gram using the apk package manager",
}
make_build_args = ["--package", "gram", "--package", "cli"]
make_check_args = [
    "--workspace",
    "--exclude=ui_macros",
    "--",
    "--skip=repository::tests::test_checkpoint_basic",
    "--skip=repository::tests::test_checkpoint_empty_repo",
    "--skip=repository::tests::test_checkpoint_exclude_binary_files",
    "--skip=repository::tests::test_compare_checkpoints",
    "--skip=project_tests::test_file_status",
    "--skip=project_tests::test_git_repository_status",
    "--skip=project_tests::test_rename_work_directory",
    "--skip=project_tests::test_staging_hunk_preserve_executable_permission",
    "--skip=gram::tests::test_window_edit_state_restoring_enabled",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "protobuf-protoc",
    "rust-bindgen",
]
makedepends = [
    "alsa-lib-devel",
    "libgit2-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "openssl3-devel",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Code editor for humanoid apes and grumpy toads, forked from Zed"
license = "GPL-3.0-only"
url = "https://gram-editor.com"
source = f"https://codeberg.org/GramEditor/gram/archive/{pkgver}.tar.gz"
sha256 = "091e2788a31261e76c01c272bdb9b4f53a3106a4c9e16dfa1318fb916e50e5bf"
# TODO(Harper): Patch message "Installation from source URL requires rustup to be installed"
# TODO(Harper): Patch in extension compilation errors that explain which packages to install


def install(self):
    self.install_file(
        f"target/{self.profile().triplet}/release/gram",
        "usr/lib/gram",
        name="gram-editor",
    )
    self.install_bin(
        f"target/{self.profile().triplet}/release/cli",
        name="gram",
    )
    self.install_file(
        "crates/gram/resources/app-icon.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        "crates/gram/resources/app-icon@2x.png",
        "usr/share/icons/hicolor/1024x1024/apps",
        name="app.liten.Gram.png",
    )
    self.install_file(
        "crates/gram/resources/gram.desktop.in",
        "usr/share/applications",
        name="app.liten.Gram.desktop",
    )
    self.install_license("LICENSE-GPL")
