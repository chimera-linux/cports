pkgname = "diff-so-fancy"
pkgver = "1.4.4"
pkgrel = 0
depends = ["perl"]
checkdepends = ["bash", "perl"]
pkgdesc = "Improved diff colorizer"
license = "MIT"
url = "https://github.com/so-fancy/diff-so-fancy"
_bats_core_url = "https://github.com/bats-core/bats-core"
_bats_core_pkgver = "1.12.0"
_bats_support_url = "https://github.com/bats-core/bats-support"
_bats_support_pkgver = "0.3.0"
_bats_assert_url = "https://github.com/bats-core/bats-assert"
_bats_assert_pkgver = "2.1.0"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"{_bats_core_url}/archive/refs/tags/v{_bats_core_pkgver}.tar.gz",
    f"{_bats_support_url}/archive/refs/tags/v{_bats_support_pkgver}.tar.gz",
    f"{_bats_assert_url}/archive/refs/tags/v{_bats_assert_pkgver}.tar.gz",
]
source_paths = [
    ".",
    "test/bats",
    "test/test_helper/bats-support",
    "test/test_helper/bats-assert",
]
sha256 = [
    "3eac2cfb3b1de9d14b6a712941985d6b240b7f3726c94a5e337317c7161e869d",
    "e36b020436228262731e3319ed013d84fcd7c4bd97a1b34dee33d170e9ae6bab",
    "7815237aafeb42ddcc1b8c698fc5808026d33317d8701d5ec2396e9634e2918f",
    "98ca3b685f8b8993e48ec057565e6e2abcc541034ed5b0e81f191505682037fd",
]


def pre_check(self):
    # TODO: apply patch here so tests don't fail
    pass


def check(self):
    self.do("./test/bats/bin/bats", "test")


def install(self):
    self.install_files("lib/DiffHighlight.pm", "usr/share/diff-so-fancy")
    self.install_bin("diff-so-fancy")
    self.install_license("LICENSE")
