pkgname = "python-hypothesis"
pkgver = "6.153.0"
pkgrel = 0
build_wrksrc = "hypothesis"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-attrs", "python-sortedcontainers", "python-watchdog"]
checkdepends = [
    "python-black",
    "python-click",
    "python-dateutil",
    "python-pexpect",
    "python-ptyprocess",
    "python-pytest",
    "python-pytest-xdist",
    "python-pytz",
    "python-typing_extensions",
    *depends,
]
pkgdesc = "Python library for property-based testing"
license = "MPL-2.0"
url = "https://hypothesis.works/index.html"
source = f"https://github.com/HypothesisWorks/hypothesis/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "42b53b37622bb27dae4bd7ca3ff6ed90f72029aa2ed8911b4802310680258197"


def init_check(self):
    self.make_check_args = [
        "--ignore=tests/array_api",
        "--ignore=tests/cover/test_custom_reprs.py",  # needs pytest-snapshot
        "--ignore=tests/cover/test_filestorage.py",  # needs git
        "--ignore=tests/cover/test_reflection.py",
        "--ignore=tests/datetime/test_dateutil_timezones.py",
        "--ignore=tests/dpcontracts/test_contracts.py",
        "--ignore=tests/patching/test_patching.py",
        "--ignore=tests/conjecture/test_utils.py",
        "--ignore=tests/ghostwriter/test_expected_output.py",
        "--ignore=tests/ghostwriter/test_ghostwriter_cli.py",  # needs installed cli
        "--ignore=tests/codemods/test_codemods.py",
        "--ignore=tests/lark/test_grammar.py",
        "--ignore=tests/nocover/test_scrutineer.py",
        "--ignore=tests/redis/test_redis_exampledatabase.py",
        "--ignore=examples/example_hypothesis_entrypoint/test_entrypoint.py",
        "--ignore=tests/codemods/test_codemod_cli.py",
        "--ignore=tests/cover/test_database_backend.py",
        "--ignore=tests/cover/test_observability.py",
        "--ignore=tests/watchdog/test_database.py",
        "--ignore=tests/snapshots/test_always_failing.py",  # needs pytest-snapshot
        "--ignore=tests/snapshots/test_combinators.py",  # ditto
        "--ignore=tests/snapshots/test_shrinking.py",  # ditto
        "--ignore=tests/snapshots/test_explain.py",  # ditto
        "--ignore=tests/pandas",
        "--ignore=tests/numpy",
        "--ignore=tests/scipy",
        "--ignore=tests/crosshair",
        "-k",
        # XXX: fails because posix/ tzdata folder doesn't exist
        "not test_can_generate_prefixes_if_allowed_and_available",
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]
