pkgname = "rustypaste"
pkgver = "0.15.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=openssl",
]
make_install_args = [*make_build_args]
make_check_args = [
    *make_build_args,
    "--",
    "--test-threads=1",
    # both make remote requests to wikimedia
    "--skip=paste::tests::test_paste_data",
    "--skip=server::tests::test_upload_remote_file",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
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
sha256 = "a1f1afe2154ec5cc78da02dbb98c6069331b149cdfaf8975ffb73ac8fdf8d60d"


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "rustypaste")
    self.install_file("config.toml", "etc/rustypaste")
