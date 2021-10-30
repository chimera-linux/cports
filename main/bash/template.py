pkgname = "bash"
pkgver = "5.1.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-bash-malloc",
    "--with-curses",
    "--without-installed-readline",
    "gl_cv_func_working_acl_get_file=yes",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
make_check_target = "tests"
hostmakedepends = ["bison", "texinfo"]
makedepends = ["ncurses-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU Bourne Again Shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bash"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "0cfb5c9bb1a29f800a97bd242d19511c997a1013815b805e0fdd32214113d6be"

def init_configure(self):
    tcap = self.profile().sysroot / "usr/lib/libncursesw.a"
    self.make_build_args += [f"TERMCAP_LIB={tcap}"]

def post_install(self):
    self.install_dir("etc/bash/bashrc.d")
    (self.destdir / "etc/bash/bashrc.d/.empty").touch()
    (self.destdir / "etc/bash/bashrc.d/.empty").chmod(0o644)

    # register with shells
    self.install_dir("etc/shells.d")
    self.install_link("/usr/bin/bash", "etc/shells.d/bash")

    self.rm(self.destdir / "usr/share/doc", recursive = True, force = True)

    self.install_link("bash", "usr/bin/rbash")

    self.install_file(self.files_path / "bashrc", "etc/bash")
    self.install_file(self.files_path / "bash.sh", "etc/profile.d")

    # remove devel files
    self.rm(self.destdir / "usr/lib", recursive = True)
    self.rm(self.destdir / "usr/include", recursive = True)
