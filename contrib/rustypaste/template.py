pkgname = "rustypaste"
pkgver = "0.15.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=openssl",
]
make_install_args = list(make_build_args)
make_check_args = make_build_args + [
    "--",
    "--test-threads=1",
    # both make remote requests to wikimedia
    "--skip=paste::tests::test_paste_data",
    "--skip=server::tests::test_upload_remote_file",
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
sha256 = "d2f23fa70f389dc0e57606799e780ba7bcfc648514e72de55154ccf5571fc6cf"


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
