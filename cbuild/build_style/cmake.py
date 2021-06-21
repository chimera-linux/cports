from cbuild.util import make
import os

def init_configure(self):
    self.make = make.Make(self, wrksrc = "build")

def do_configure(self):
    if self.cmake_dir:
        cdir = str(self.chroot_wrksrc / self.cmake_dir)
    else:
        cdir = str(self.chroot_wrksrc)

    os.makedirs(self.abs_build_wrksrc / "build", exist_ok = True)

    self.do(
        "cmake", [
            "-DCMAKE_INSTALL_PREFIX=/usr",
            "-DCMAKE_BUILD_TYPE=None",
            "-DCMAKE_INSTALL_LIBDIR=lib",
            "-DCMAKE_INSTALL_SBINDIR=bin"
        ] + self.configure_args + [cdir],
        wrksrc = "build", build = True, env = {
            "CMAKE_GENERATOR": (
                "Ninja" if self.make_cmd == "ninja" else "Unix Makefiles"
            )
        }
    )

def do_build(self):
    self.make.build()

def do_check(self):
    pass

def do_install(self):
    if self.make_cmd == "ninja":
        self.make.install(default_args = False, env = {
            "DESTDIR": str(self.chroot_destdir)
        })
    else:
        self.make.install()

def use(tmpl):
    tmpl.build_style = "cmake"
    tmpl.init_configure = init_configure
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
    tmpl.make_build_target = "all"
    tmpl.make_cmd = "ninja"

    tmpl.build_style_fields = [
        ("cmake_dir", None, str, False, False, False)
    ]
