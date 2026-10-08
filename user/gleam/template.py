pkgname = "gleam"
pkgver = "1.19.1"
pkgrel = 0
build_style = "cargo"
make_check_args = [
    "--",
    # overflows the stack on ppc64le
    "--skip=type_::tests::no_stack_overflow_for_nested_use",
    # checks files that would be git ingored, but the tarball is not a git repo
    "--skip=tests::all_files_have_copyright_notice",
    # tries to access network to fetch dependency
    "--skip=tests::escript_success_with_dependency",
    # tries to access network to choose version of gleam_stdlib
    "--skip=tests::output::echo_dict",
]
hostmakedepends = ["cargo-auditable"]
checkdepends = ["erlang", "git", "nodejs"]
depends = ["erlang"]
pkgdesc = "Friendly language for building scalable type-safe systems"
license = "Apache-2.0"
url = "https://gleam.run"
source = (
    f"https://github.com/gleam-lang/gleam/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5a717b4013d5599d73a99b3a1a4bb9168e62bfc18afff2f5bbab43244f860df0"


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "aws-lc-sys-0.44.0")


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "gleam"))
