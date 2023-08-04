from cbuild.util import cmake, make


def do_configure(self):
    cmake.configure(self, self.cmake_dir)


def do_build(self):
    self.make.build()


def do_check(self):
    cmake.ctest(self)


def do_install(self):
    self.make.install(args_use_env=(self.make_cmd == "ninja"))


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl)

    tmpl.build_style_defaults = [
        ("make_cmd", "ninja"),
        ("make_build_target", "all"),
        ("make_dir", "build"),
    ]
