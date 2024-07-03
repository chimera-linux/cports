pkgname = "borg"
pkgver = "1.4.0"
pkgrel = 0
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
    + " and not test_convert_all",
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
source = f"https://github.com/borgbackup/borg/archive/tags/{pkgver}.tar.gz"
sha256 = "34fa63c8921ad7c6c1eadc3029ed3261a8494f9c264f900d7079197a1584bcd5"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("scripts/shell_completions/bash/borg", "bash")
    self.install_completion("scripts/shell_completions/fish/borg.fish", "fish")
    self.install_completion("scripts/shell_completions/zsh/_borg", "zsh")
