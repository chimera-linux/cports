pkgname = "jaq"
pkgver = "3.1.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features", "--bin", "jaq"]
make_install_args = [*make_build_args]
make_check_args = ["--no-default-features"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/jaq.1",
]
source_paths = [".", "manpage"]
sha256 = [
    "8ad074d7e90e07ad7e77048dcf0d0e7ad434b8e3e38044260b9457d4551e644d",
    "01c39aa68e2086d3dfe88031984f25cd1eb6d3f146b371f55c7c4e9ba2dbfa77",
]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jaq")
    self.install_man(self.sources_path / "jaq.1")
    self.install_license("LICENSE-MIT")
