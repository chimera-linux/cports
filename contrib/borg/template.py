pkgname = "borg"
pkgver = "1.2.8"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {
    "BORG_LIBLZ4_PREFIX": "/usr/include",
    "BORG_ZSTD_PREFIX": "/usr/include",
    "BORG_XXHASH_PREFIX": "/usr/include",
}
make_check_args = [
    "--pyargs",
    "borg.testsuite",
    "--benchmark-skip",
    # these take forever
    "-k",
    "not test_prune_retain_and_expire_oldest and not test_prune_repository_example",
    "--dist=worksteal",
]
make_check_env = {"BORG_FUSE_IMPL": "none"}
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-pkgconfig",
    "python-setuptools_scm",
    "python-wheel",
]
makedepends = [
    "acl-devel",
    "linux-headers",
    "lz4-devel",
    "openssl-devel",
    "python-devel",
    "xxhash-devel",
    "zstd-devel",
]
depends = ["python-packaging", "python-msgpack", "python-pyfuse3"]
checkdepends = [
    "python-dateutil",
    "python-pytest-benchmark",
    "python-pytest-xdist",
] + depends
pkgdesc = "Deduplicating backup program"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://www.borgbackup.org"
source = f"https://github.com/borgbackup/borg/releases/download/{pkgver}/borgbackup-{pkgver}.tar.gz"
sha256 = "d39d22b0d2cb745584d68608a179b6c75f7b40e496e96feb789e41d34991f4aa"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("scripts/shell_completions/bash/borg", "bash")
    self.install_completion("scripts/shell_completions/fish/borg.fish", "fish")
    self.install_completion("scripts/shell_completions/zsh/_borg", "zsh")
