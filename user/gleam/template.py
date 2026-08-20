pkgname = "gleam"
pkgver = "1.18.1"
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
sha256 = "0691b50bd3592a549abbbd7a0dea4b11f8930988c1e398d1d1429faf48933a3c"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/gleam")
