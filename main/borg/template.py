pkgname = "borg"
pkgver = "1.4.1"
pkgrel = 2
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
make_check_args = [
    "--pyargs",
    "borg.testsuite",
    "--benchmark-skip",
    "-k",
    # these take forever
    "not test_prune_retain_and_expire_oldest and not test_prune_repository_example"
    # these require files that aren't copied to the checkenv
    + " and not test_detect_attic_repo"
    + " and not test_key_export_qr"
    + " and not test_convert_segments"
    + " and not test_keys"
    + " and not test_convert_all"
    # flaky
    + " and not test_corrupted_repository",
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
    "openssl3-devel",
    "python-devel",
    "xxhash-devel",
    "zstd-devel",
]
depends = [
    "python-msgpack",
    "python-packaging",
    "python-pyfuse3",
]
checkdepends = [
    "python-dateutil",
    "python-pytest-benchmark",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Deduplicating backup program"
license = "BSD-3-Clause"
url = "https://www.borgbackup.org"
source = f"https://github.com/borgbackup/borg/archive/tags/{pkgver}.tar.gz"
sha256 = "bf492c900d4eacce099639509e77caaf05edf74966a1c3153a36c63779aee10b"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("scripts/shell_completions/bash/borg", "bash")
    self.install_completion("scripts/shell_completions/fish/borg.fish", "fish")
    self.install_completion("scripts/shell_completions/zsh/_borg", "zsh")
    self.install_man("docs/man/*", glob=True)
