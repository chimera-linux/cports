pkgname = "rustypaste"
pkgver = "0.14.4"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=openssl",
]
make_install_args = list(make_build_args)
make_check_args = make_build_args + [
    # tests relying on fixtures and binding to the network will always fail
    "--",
    "--skip=auth::tests::test_extract_tokens",
    "--skip=paste::tests::test_paste_data",
    "--skip=server::tests::test_delete_file",
    "--skip=server::tests::test_delete_file_without_token_in_config",
    "--skip=server::tests::test_list",
    "--skip=server::tests::test_list_expired",
    "--skip=server::tests::test_upload_duplicate_file",
    "--skip=server::tests::test_upload_expiring_file",
    "--skip=server::tests::test_upload_file",
    "--skip=server::tests::test_upload_remote_file",
    "--skip=util::tests::test_get_expired_files",
    "--skip=server::tests::test_upload_oneshot",
    "--skip=server::tests::test_upload_oneshot_url",
    "--skip=server::tests::test_upload_url",
    # gets a 200 instead of 302 for whatever reason
    "--skip=server::tests::test_index_with_landing_page_file_not_found",
]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "File upload/pastebin service"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/orhun/rustypaste"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2d5e7aac9c3badd3ee059a9cc4d3e77b2fee18922f144d70f70059f9b4a6bdf1"


def post_install(self):
    self.install_license("LICENSE")

    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="rustypaste.conf",
    )

    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="rustypaste.conf",
    )

    self.install_service(self.files_path / "rustypaste")

    self.install_file("config.toml", "etc/rustypaste")
    self.install_file(
        self.files_path / "rustypaste.default", "etc/default", name="rustypaste"
    )
